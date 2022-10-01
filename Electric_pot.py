import numpy as np


def Electric_pot(x_1, y_1, x_2, y_2, q):
    """Calculates the electric potential at point(s) (x_2, y_2)"""
    ep_0 = 8.854 * 10 ** -12  # C^2/(N * m^2)
    r = np.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
    pot_denom = 4 * np.pi * ep_0 * r
    return(q / pot_denom)
