import numpy as np
from vpython import sphere, vector, rate

L = 101
i = 50
j = 50

point = sphere(make_trail=True)
point.p = vector(i, j, 0)
a = vector(50, 50, 0)
for steps in np.arange(1e6):
    rate(40)
    point.pos = vector(i - 50, j - 50, 0)
    z = np.random.randint(1, 5)
    if z == 1:
        if z == L:
            continue
        i += 1
    if z == 2:
        if z == 0:
            continue
        i -= 1
    if z == 3:
        if z == L:
            continue
        j += 1
    if z == 4:
        if z == 0:
            continue
        j -= 1