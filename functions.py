import math
import numpy as np


def rosenbrocks(variables_values):
    (x, y) = variables_values
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def rosenbrocks_f(X, Y):
    f = []

    for i in range(250):
        for j in range(250):
            x = X[i][j]
            y = Y[i][j]
            f.append((1 + x) ** 2 + 100 * (y - x ** 2) ** 2)

    return np.reshape(f, (250, 250))


def sphere(variables_values):
    (x, y) = variables_values
    return x ** 2 + y ** 2


def sphere_f(X, Y):
    f = []

    for i in range(250):
        for j in range(250):
            x = X[i][j]
            y = Y[i][j]
            f.append(x ** 2 + y ** 2)

    return np.reshape(f, (250, 250))


def beale(variables_values):
    (x, y) = variables_values
    return (1.5 - x + x*y) ** 2 + (2.25 - x + x*y ** 2) ** 2 + (2.625 - x + x*y ** 3) ** 2


def beale_f(X, Y):
    f = []

    for i in range(250):
        for j in range(250):
            x = X[i][j]
            y = Y[i][j]
            f.append((1.5 - x + x*y) ** 2 + (2.25 - x + x*y ** 2) ** 2 + (2.625 - x + x*y ** 3) ** 2)

    return np.reshape(f, (250, 250))


def goldstein_price(variables_values):
    (x, y) = variables_values
    return (1 + (x + y + 1) ** 2 * (19 - 14*x + 3*x*x - 14*y + 6*x*y + 3*y*y)) * \
           (30 + (2*x - 3*y) ** 2 * (18 - 32*x + 12*x*x + 48*y - 36*x*y + 27*y*y))


def goldstein_price_f(X, Y):
    f = []

    for i in range(250):
        for j in range(250):
            x = X[i][j]
            y = Y[i][j]
            f.append((1 + (x + y + 1) ** 2 * (19 - 14*x + 3*x*x - 14*y + 6*x*y + 3*y*y)) *
                     (30 + (2*x - 3*y) ** 2 * (18 - 32*x + 12*x*x + 48*y - 36*x*y + 27*y*y)))

    return np.reshape(f, (250, 250))


def three_hump_camel(variables_values):
    (x, y) = variables_values
    return 2*x*x - 1.05*x ** 4 + x ** 6 / 6 + x*y + y*y


def three_hump_camel_f(X, Y):
    f = []

    for i in range(250):
        for j in range(250):
            x = X[i][j]
            y = Y[i][j]
            f.append(2*x*x - 1.05*x ** 4 + x ** 6 / 6 + x*y + y*y)

    return np.reshape(f, (250, 250))
