# Algorithm to solve X^2-x-2=0 (Guesses [1,3])

import math

def func(x):
    return x**2 - x - 2 

def regula_falsi(a, b, no_of_iterations, tol):
    fa = func(a)
    fb = func(b)

    for i in range(no_of_iterations):
        x = (fa * b - fb * a) / (fa - fb)
        fx = func(x)

        if abs(fx) < tol:
            return x
        
        if fa * fx < 0:
            b = x
            fb = fx
        
        else:
            a = x
            fa = fx

        print(f"no_of_iterations {i+1} : x = {x}, fx = {fx}")
    return x

#Initialize the values of the guesses and number of iterations

a = 1
b = 3
no_of_iterations = 3
tol = 1e-6

root = regula_falsi(a,b,no_of_iterations,tol)
print(f"Approximate root after {no_of_iterations} iterations: {root}")