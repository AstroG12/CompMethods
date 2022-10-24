from Newton_Method import newton_method
from Lagrange import lagrange_point
from relaxation import relax

# Constants that are used

# r = 384400.0e3 * 0.80
r = 350000000
h = 1e2
sol = newton_method(lagrange_point, x=r, h=h)
print("Using Newton's method we find a solution of {} and when plugged into my Lagrange eq yields {}".format(sol, lagrange_point(sol)))
print(sol, lagrange_point(sol))
print(" ")
r_sol = relax(lagrange_point, x=r)
print("Using Relaxation method we find a solution of {} and when plugged into my Lagrange eq yields {}".format(r_sol, lagrange_point(r_sol)))
print(r_sol, lagrange_point(r_sol))