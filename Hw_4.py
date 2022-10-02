from Newton_Method import newton_method
from Lagrange import lagrange_point

# Constants that are used

r = 384400.0e3 * 0.80
sol = newton_method(lagrange_point, x=r)
print(sol, lagrange_point(sol))
