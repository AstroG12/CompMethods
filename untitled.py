import numpy as np
from Electric_pot import Electric_pot
import matplotlib.pyplot as plt

x = np.linspace(-1.0, 1.0, 3)
y = np.linspace(-1.0, 1.0, 3)
X, Y = np.meshgrid(x, y)
pot = Electric_pot(0.2, 0, X, Y, 1)
grad = np.gradient(pot)


def Grad(X, h):
    """
    Calcuclates graduate
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
            dy[z, k] = (X[z, k_1] - X[z, k-1]) / h
    return(dx, dy)


dx_1 = (pot[0, 1] - pot[0, -1]) / (0.1)
new = Grad(pot, 1)
print(new[0])
print(new[1])
print(X)
print(" ")
print(Y)
print(" ")
print(pot.T)
print(" ")
print(grad[0])
print(" ")
print(grad[1])
print(dx_1)
plt.streamplot(X, Y, new[0], new[1])
plt.show()
