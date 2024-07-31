# Value of y at x = 4.0
#Linear spline formula

import numpy as np
import matplotlib.pyplot as plt

x_coordinates = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_coordinates = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

x_to_find = 4.0

for i in range(len(x_coordinates) -1):
    if x_coordinates[i] <= x_to_find <= x_coordinates[i + 1]:
        x1, y1 = x_coordinates[i], y_coordinates[i]
        x2, y2 = x_coordinates[i+1], y_coordinates[i+1]
        break
    
y_to_find = y1 + (y2 - y1) / (x2 - x1) * (x_to_find - x1)
print(f'The value of y at x = {x_to_find} is approximately {y_to_find:.2f}')

plt.plot(x_coordinates, y_coordinates, 'o-' , label= 'Hole centers')
plt.plot(x_to_find, y_to_find, 'rx' , label= f'interpolated y at x={x_to_find}')
plt.xlabel('X (in)')
plt.ylabel('Y (in)')
plt.legend()
plt.grid(True)
plt.show()