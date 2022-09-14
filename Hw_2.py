import numpy as np 
import matplotlib.pyplot as plt

# create function
def f(x):
	return(np.exp(-x**2))

# Trap rule 
def Trap(func, a, b, N):
	h = (b - a) / N

	s = 0.5 * (func(a) + func(b))

	for i in range(1,N):
		s += func(a + i * h)
	return(s*h)

def Simp(func, a, b, N):
	h = (b - a) / N

	s = (func(a) + func(b))

	for k in range(1,N):
		if k%2 == 0:
			s += 2 * func(a + (k * h))
		else:
			s += 4 * func(a + (k * h)) 
	return(s*h/3)

x_terms = [x/10 for x in range(1,30)]
y_trap = []
y_simp = []

for x in x_terms:
	y_trap.append(Trap(f,0,x,30))
	y_simp.append(Simp(f,0,x,30))

fig, (ax_1,ax_2) = plt.subplots(2, sharex=True)
ax_1.plot(x_terms,y_trap,color="#009E73")
ax_1.text(0.3,0.2,"Trapazoid = {}".format(Trap(f,0,3,30)))
ax_1.set_title("Trapazoid Method")
ax_2.plot(x_terms,y_simp,color="#D55E00")
ax_2.text(0.3,0.2,"Simpson's = {}".format(Simp(f,0,3,30)))
ax_2.set_title("Simpson's Method")
ax_2.set_xlabel("X")
plt.show()






