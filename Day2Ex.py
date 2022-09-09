# imports
import numpy as np

def quad(a, b, c):
	"""Returns zeroes of func"""
	x1 = (-b + np.sqrt((b**2) - (4*a*c))) / 2 * a
	x2 = (-b - np.sqrt((b**2) - (4*a*c))) / 2 * a
	return (x1, x2)

def Num_check(a):
	if a < 0:
		print("{} is negative".format(a))
	elif a > 0:
		print("{} is postive".format(a))
	else:
		print("value is 0")

def X_check():
	for i in range(0,21):
		if i%2 != 0:
			print(i)


def grav(h,g=9.8):
	return(np.sqrt(2 * h / g))