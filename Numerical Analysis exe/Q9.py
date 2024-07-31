#computing the coefficients of the lagrange polynomial

import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x):
  
    n = len(x_points)
    result = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term = term * (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

x_points = np.array([1, 2, 3, 4])
y_points = np.array([1, 4, 9, 16])

x_range = np.linspace(1, 4, 100)
y_range = [lagrange_interpolation(x_points, y_points, x) for x in x_range]


plt.plot(x_points, y_points, 'o', label='Data points')
plt.plot(x_range, y_range, label='Lagrange polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Lagrange Polynomial Interpolation')
plt.grid(True)
plt.show()
