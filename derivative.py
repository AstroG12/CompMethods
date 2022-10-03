def der(func, x, h):
    return(func(x + h) - func(x - h) / (2 * h))
