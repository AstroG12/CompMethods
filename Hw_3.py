import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "helvetica"
plt.style.use('seaborn-white')


def Electric_pot(q,x_1,y_1,x_2,y_2):
	"""Calculates the electric potential at points x_2 and y_2"""
	ep_0 = 8.854 * 10**-12 #C^2/(N * m^2)
	return(q / (4 * np.pi * ep_0 * np.sqrt(((x_2 - x_1)**2) + ((y_2 - y_1)**2))))

# point charge 1 info

dist_1 = 1 

# point charge 2 info

dist_2 = -1 

# Creating points in a square grid 

x = np.linspace(-2,2,15)
y = np.linspace(-2,2,15)
X,Y = np.meshgrid(x,y)

# Calculating electric potential at all points

potential = Electric_pot(1,-1.2,0,X,Y) + Electric_pot(1,1.2,0,X,Y)

# Calculating the E field at those points & and the speed for vector field

field = np.gradient(potential)

speed = np.sqrt(field[0]**2 + field[1]**2)

# Create figure

fig, axes = plt.subplots(nrows=2,ncols=2,figsize=(11,11),gridspec_kw={
                           'width_ratios': [5, 5],
                           'height_ratios': [5, 5]})

axes[1,1].axis("off")

# Plot the points made(gray) and particle (red and blue)

axes[0,0].scatter(X,Y,color="grey")
axes[0,0].grid()
axes[0,0].scatter(dist_1, 0, color="r")
axes[0,0].scatter(dist_2, 0, color="b")
axes[0,0].title.set_text("Points to Find Potentials")
axes[0,0].set_xlabel("X")
axes[0,0].set_ylabel("Y")

# Plots image of potential 

cmap=axes[0,1].imshow(potential/1e10,vmin=0,vmax=5,extent=[0,2,0,2],origin="lower",cmap="copper_r")
axes[0,1].title.set_text("Map of Potentials(Volts * 10^10)")
axes[0,1].set_xlabel("X")
axes[0,1].set_ylabel("Y")

# Plots E-field

# lw = 5*speed / speed.max()
# axes[1,0].streamplot(X,Y,field[0],field[1],color="k",linewidth=lw)
axes[1,0].streamplot(X,Y, field[0],field[1],color="k" ,density=[0.5, 1])
axes[1,0].scatter(1, 0, color="r")
axes[1,0].scatter(-1, 0, color="b")
axes[1,0].title.set_text("Electric Field")
axes[1,0].set_xlabel("X")
axes[1,0].set_ylabel("Y")

plt.colorbar(cmap,ax=axes[0,1],fraction=0.046,pad=0.04)
fig.suptitle("Homework #3")
plt.show()