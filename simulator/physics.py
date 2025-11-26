import numpy as np
from scipy.integrate import solve_ivp


class PhysicsEngine:

    def __init__(self, fd_solver, gravity=[0.0, -9.81, 0.0]):
        self.fd_solver = fd_solver
        self.gravity = np.array(gravity)

    def update(self, objects, dt):

        if not objects:
            return

        for obj in objects:
            
            # tau = np.zeros(obj.qd.shape)
            tau = - 10.0  * np.diag(np.random.random(len(obj.qd))-0.5) @ obj.qd
            # tau = - 0.5 * obj.qd
            # tau = 100.0 * (1.57 * np.ones_like(obj.q) - obj.q) - 20.0 * obj.qd
            # tau = 100.0 * (3*np.random.random(len(obj.q)) - obj.q) - 20.0 * obj.qd

            # tree7
            # tau = 100.0 * (np.array([-1.57, 0.0, 0.707, -0.707, 0.707, -0.707, 0.707, -0.707]) - obj.q) - 20.0 * obj.qd

            # ddq = self.fd_solver.forward_dynamics(obj, obj.q, obj.qd, tau)
            # obj.qd += ddq * dt
            # obj.q += obj.qd * dt


            def dynamics(t, y):
                    dof = len(y) // 2
                    q = y[:dof]
                    qd = y[dof:]
                    
                    ddq = self.fd_solver.forward_dynamics(obj, q, qd, tau)
                    
                    return np.hstack((qd, ddq))


            y0 = np.hstack((obj.q, obj.qd))

            sol = solve_ivp(
                dynamics,
                t_span=(0, dt),
                y0=y0,
                method='RK45',
                max_step=dt
            )

            dof = len(obj.q)
            obj.q = sol.y[:dof, -1]
            obj.qd = sol.y[dof:, -1]