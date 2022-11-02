import numpy as np

np.random.seed(69420)

z = np.random.random(10**3)
x = z**2
g = 1 / (np.exp(x) + 1)
I = 2 * sum(g) / len(g)

print("The integral is ~ {}".format(I))
