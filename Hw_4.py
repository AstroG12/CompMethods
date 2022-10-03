from Newton_Method import newton_method
from Lagrange import lagrange_point
from relaxation import relax

# Constants that are used

# r = 384400.0e3 * 0.80
r = 350000000
h = 1e7
sol = newton_method(lagrange_point, x=r, h=h)
print(sol, lagrange_point(sol))
print(" ")
r_sol = relax(lagrange_point, x=r)
print(r_sol, lagrange_point(r_sol))