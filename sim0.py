import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# SOLID
# S - функция, класс, модуль - единая отвественнось

#     rederer
#     physics engine
#     data

# O - 
# L

#     Транспорт()
        

#     Автомобиль(model)
#         drive()

#     Самолет(model)
#         fly()
#     Подводная лодка(модельть)

#     Транспорт obj1 = Автомобиль(.)
#     Транспорт obj2 = Самолет(.)

#     obj1.method()

# I
#     Транспорт()

#     Автомобиль(model)
#         drive()

#     Самолет(model)
#         fly()
# D

#     hight level control
#     API
#     low level control


# DRY
# YAGNI
# KISS

R = 0.2
m = 1.0
I = 0.4 * m * R**2

R2 = 0.3
m2 = 1.0
I2 = 0.4 * m2 * R2**2


g = 9.81

dt = 0.01

r = np.array([0.0, 5.0])
v = np.array([0.0, 0.0])
omega = 5.0

r2 = np.array([2.0, 5.0])
v2 = np.array([0.0, 0.0])
omega2 = 5.0

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

ball_patch = Circle(r, R, color="red")
ax.add_patch(ball_patch)

ball_patch2 = Circle(r2, R2, color="blue")
ax.add_patch(ball_patch2)


for _ in range(500):

    Fg = np.array([0, -m * g])
    dv = Fg / m

    v += dv * dt
    r += v * dt

    Fg2 = np.array([0, -m2 * g])
    dv2 = Fg2 / m2

    v2 += dv2 * dt
    r2 += v2 * dt

    M = 0
    domega = M / I
    omega += domega * dt

    ball_patch.center = r

    ball_patch2.center = r2

    plt.pause(0.001)

plt.show()


