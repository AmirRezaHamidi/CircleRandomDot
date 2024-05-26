import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time

n_iteration = 10000
start = 0
step = 0.01
stop = 2*math.pi + step

border = np.arange(start, stop, step)
x_border = np.cos(border)
y_border = np.sin(border)

c_points = [math.pi* 1/2, math.pi * 7/6, math.pi * 11/6]
x_c_points = np.cos(c_points)
y_c_points = np.sin(c_points)

x_current_point = random.random() * 2 - 1
y_current_point = random.random() * 2 - 1

x_points = list()
y_points = list()
figure, ax = plt.subplots(figsize=(10, 8))

for _ in range(n_iteration):

    index = random.choice([0, 1, 2])
    c_point_x = x_c_points[index]
    c_point_y = y_c_points[index]

    x_mid_point = (c_point_x + x_current_point) / 2
    y_mid_point = (c_point_y + y_current_point) / 2

    x_points.append(x_mid_point)
    y_points.append(y_mid_point)

    x_current_point = x_mid_point
    y_current_point = y_mid_point

ax.scatter(x_points, y_points)
plt.show()


# ploting

# x_plotting = list()
# y_plotting = list()

# plt.ion()
# figure, ax = plt.subplots(figsize=(10, 8))
# plot, = ax.plot(x_points, y_points)

# ax.plot(x_c_points, y_c_points, "r.")
# ax.plot(x_border, y_border, "k-")

# for i in range(n_iteration):

#     plot.set_xdata(x_points[0:i])
#     plot.set_ydata(*y_points[0:i])

#     figure.canvas.draw()
#     figure.canvas.flush_events()
#     time.sleep()
