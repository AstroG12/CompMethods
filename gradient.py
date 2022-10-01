import numpy as np


def Grad(X, h):
    """
    Calcuclates graduate for a 2 dim matrix 
    """
    dx = np.empty(X.shape, float)
    dy = np.empty(X.shape, float)
    for j in range(len(dx)):
        for i in range(len(dx)):
            x_1 = i + 1
            if x_1 >= len(dx):
                x_1 = 0
            dx[i, j] = (X[x_1, j] - X[i - 1, j]) / h
    for z in range(len(dy)):
        for k in range(len(dy)):
            k_1 = k + 1
            if k_1 >= len(dy):
                k_1 = 0
            dy[z, k] = (X[z, k_1] - X[z, k - 1]) / h
    return(dx, dy)
    