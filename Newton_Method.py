from derivative import der
import numpy as np


def newton_method(func, x, h):
    """
    Preforms Newton's method on a given function with initial guess
    x. I would recommend starting high-ish with guess until I decide
    to make it better....
    """
    while np.abs(func(x)) > 1e-3:
        x -= func(x) / der(func, x, h)
    return(x)
