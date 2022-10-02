from astropy.constants import G, M_earth


def lagrange_point(r, R=384400.0e3, m=7.34767e22, M=M_earth.value):
    """
    This is just the left hand side of the equation
    to find a true lagrange point the r must satisfy
    L = 0.
    """
    w = 2.662e-6
    L_term1 = (G.value * M) / (r ** 2)
    L_term2 = (G.value * m) / ((R - r) ** 2)
    L_term3 = (w ** 2) * r
    return(L_term1 - L_term2 - L_term3)
