import numpy as np
import matplotlib.pyplot as plt
from math import log


def f(x):
    return x**2

def g(x):
    y = np.log(x)
    return x*y
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 2000, 100)
z = g(x)
# Plot the points using matplotlib
plt.plot(x, f(x),marker='o')
plt.plot(x, z,marker='o')

plt.show()  # You must call plt.show() to make graphics appear.