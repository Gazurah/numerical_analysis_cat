import numpy as np

def trapezoidal_rule(func, a, b, n):
  
    h = (b - a) / n

    integral_sum = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        integral_sum += func(a + i * h)

    integral_value = h * integral_sum

    return integral_value

if __name__ == "__main__":
    def f(x):
        return np.sin(x)

    a = 0.0
    b = np.pi
    n = 100

    integral_approx = trapezoidal_rule(f, a, b, n)

    print(f"Approximate integral of sin(x) from {a} to {b} using {n} subintervals: {integral_approx}")
