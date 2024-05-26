import numpy as np
import matplotlib.pyplot as plt
import random
import math

n_iteration = 1000
start = 0
step = 0.01
stop = 2*math.pi + step

circle_linespace = np.arange(start, stop, step)
x_border = np.cos(circle_linespace)
y_border = np.sin(circle_linespace)
plt.plot(x_border, y_border, "k.")

c_points = [math.pi* 1/2, math.pi * 7/6, math.pi * 11/6]
x_c_points = np.cos(c_points)
y_c_points = np.sin(c_points)
plt.plot(x_c_points, y_c_points, "r.")


x_point = random.random() * 2 - 1
y_point = random.random() * 2 - 1

x_points = list()
y_points = list()

plt.plot(x_point, y_point, "b.")

for _ in range(n_iteration):

    index = random.choice([0, 1, 2])
    c_point_x = x_c_points[index]
    c_point_y = y_c_points[index]

    x_mid_point = (c_point_x + x_point) / 2
    y_mid_point = (c_point_y + y_point) / 2

    x_points.append(x_mid_point)
    y_points.append(y_mid_point)

    x_point = x_mid_point
    y_point = y_mid_point

plt.plot(x_points, y_points, "r ")
plt.show()