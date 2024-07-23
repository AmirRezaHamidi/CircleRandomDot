import numpy as np
import matplotlib.pyplot as plt
import random
import math
from matplotlib.animation import FuncAnimation

# Point Calculation
n_iteration = 10000000
start = 0
step = 0.01
stop = 2 * math.pi + step

border = np.arange(start, stop, step)
x_border = np.cos(border)
y_border = np.sin(border)

c_points = [math.pi * 1/2, math.pi * 7/6, math.pi * 11/6]
x_c_points = np.cos(c_points)
y_c_points = np.sin(c_points)

index = random.choice([0, 1, 2])

x_current_point = x_c_points[index]
y_current_point = y_c_points[index]

x_points = list()
y_points = list()

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

# Plotting


def animation_function(i):

    print(i + 1, f"/ {n_partition}")
    s = i * plot_step
    e = (i + 1) * plot_step
    ax.scatter(x_points[s: e], y_points[s: e], s=1, color="b")


plot_step = int(n_iteration / 200)
n_partition = int(n_iteration / plot_step)

fig, ax = plt.subplots(figsize=(6, 6))
plt.style.use("seaborn-v0_8")
animation = FuncAnimation(fig, animation_function,
                          frames=range(n_partition),
                          interval=1, repeat=False)

ax.plot(x_c_points, y_c_points, "r.")
ax.plot(x_border, y_border, "k-")
ax.set_xlim(-1.02, 1.02)
ax.set_ylim(-1.02, 1.02)

plt.show()
