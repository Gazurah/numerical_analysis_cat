#DIFFERENTIATION

def forward_difference(f, x, h=1):
    return (f(x + h) - f(x)) / h


def func(x):
    return x**2-x-2

x = 1.0
derivative_forward = forward_difference(func, x)
print(f"forward difference method: f'({x}) = {derivative_forward}")