# Numerical Integration

import numpy as np
def trapezoidal_rule(f, a, b, n=5):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1,n):
        integral += f(a + i * h)
        return integral * h
    
def func(x):
    return x**2

a,b = 0,1
integral = trapezoidal_rule(func, a, b)
print(f"Approximate: {integral}")
