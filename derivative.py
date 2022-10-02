def der(func, x):
    h = 1e-5
    return(func(x + h) - func(x - h) / (2 * h))
