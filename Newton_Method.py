from derivative import der


def newton_method(func, x):
    """
    Preforms Newton's method on a given function with initial guess
    x. I would recommend starting high-ish with guess until I decide
    to make it better....
    """
    while func(x) > 0.002:
        x -= func(x) / der(func, x)
    return(x)
