"""
(*) For the second problem, visualize it with turtle (or any other library you like).
Draw an XOY coordinate plane and plot points on this plane.
Color the points that satisfy the condition math.sqrt(a ** 2 + b ** 2) <= 1 red, the rest green.
"""

import numpy as np
import matplotlib.pyplot as plt

step = 0.02
a = np.arange(0, 1 + step, step)
b = np.arange(0, 1 + step, step)

A, B = np.meshgrid(a, b)

distances = np.sqrt(A**2 + B**2)

plt.figure(figsize=(10, 10))

red_points = plt.scatter(A[distances <= 1], B[distances <= 1],
                        c='red', s=10, label='Inside circle')
green_points = plt.scatter(A[distances > 1], B[distances > 1],
                          c='green', s=10, label='Outside circle')

plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)

plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)

plt.xlabel('a')
plt.ylabel('b')
plt.title('Points Colored by Distance from Origin\nRed: √(a² + b²) ≤ 1, Green: √(a² + b²) > 1')
plt.legend()

plt.axis('equal')

plt.show()

# This condition actually checks if the point is inside the circle with radius 1. So I just drew quarter of the circle (first quarter of coordinate system).
# I heavily used AI for this task, because I had problems with 'turtle' module.
# This is my first time using 'numpy' and 'matplotlib' modules. Used AI to learn, I hope I did it right.