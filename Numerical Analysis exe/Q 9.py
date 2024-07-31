import numpy as np

def f(x, y):
    return x**2 + y**2 - x*y + x - y + 1

def grad_f(x, y):
    df_dx = 2*x - y + 1
    df_dy = 2*y - x - 1
    return np.array([df_dx, df_dy])

def gradient_descent(learning_rate, initial_guess, num_iterations):
    x, y = initial_guess
    for i in range(num_iterations):
        gradient = grad_f(x, y)
        x, y = x - learning_rate * gradient[0], y - learning_rate * gradient[1]
        print(f"Iteration {i+1}: x = {x}, y = {y}, f(x, y) = {f(x, y)}")
    return x, y

learning_rate = 0.1
initial_guess = np.array([0.0, 0.0])
num_iterations = 10

final_x, final_y = gradient_descent(learning_rate, initial_guess, num_iterations)
print(f"\nOptimal point: x = {final_x}, y = {final_y}, f(x, y) = {f(final_x, final_y)}")