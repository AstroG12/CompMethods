import numpy as np


def relax(func, x):
    while np.abs(func(x)) > 1e-4:
        x = func(x)
    return(x)
    