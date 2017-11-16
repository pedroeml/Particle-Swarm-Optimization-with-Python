import numpy as np

# functions we are attempting to optimize (minimize)


def sphere(x):
    total = 0

    for i in range(len(x)):
        total += x[i] ** 2

    return total


def rastrigin(x):
    return 10*len(x) + sum([(xi**2 - 10*np.cos(2*np.pi*xi)) for xi in x])


def rosenbrock(x):
    total = 0

    for i in range(len(x) - 1):
        total += 100*((x[i]**2 - x[i+1])**2) + (1 - x[i])**2

    return total
