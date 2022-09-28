import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "helvetica"
plt.style.use('seaborn-white')


def Electric_pot(q, x_1, y_1, x_2, y_2):
    """Calculates the electric potential at point(s) (x_2, y_2)"""
    ep_0 = 8.854 * 10 ** -12  # C^2/(N * m^2)
    r = np.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
    pot_denom = 4 * np.pi * ep_0 * r
    return(q / pot_denom)


# point charge 1 info
dist_1 = 0.5

# point charge 2 info

dist_2 = -0.5

# Creating points in a square grid

x = np.linspace(-1.0, 1.0, 201)
y = np.linspace(-1.0, 1.0, 201)
X, Y = np.meshgrid(x, y)

# Calculating electric potential at all points

potential = Electric_pot(1, -0.52, 0, X, Y) + Electric_pot(1, 0.52, 0, X, Y)

# Calculating the E field at those points & and the speed for vector field

field = np.gradient(potential)


# Create figure

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(11, 11), gridspec_kw={
    'width_ratios': [5, 5],
    'height_ratios': [5, 5]})

axes[1, 1].axis("off")

# Plot the points made(gray) and particle (red and blue)

axes[0, 0].scatter(X, Y, color="grey")
axes[0, 0].grid()
axes[0, 0].scatter(dist_1, 0, color="r")
axes[0, 0].scatter(dist_2, 0, color="b")
axes[0, 0].title.set_text("Points to Find Potentials")
axes[0, 0].set_xlabel("X(m)")
axes[0, 0].set_ylabel("Y(m)")

# Plots image of potential

cmap = axes[0, 1].imshow(potential / 1e10, vmin=0, vmax=5, extent=[
    0, 1, 0, 1], origin="lower", cmap="copper_r")
axes[0, 1].title.set_text("Map of Potentials (Volts * 10e10)")
axes[0, 1].set_xlabel("X(m)")
axes[0, 1].set_ylabel("Y(m)")

# Plots E-field

axes[1, 0].streamplot(X, Y, field[0] * -1, field[1] * -1, color="k", density=[
    0.5, 1])
axes[1, 0].scatter(dist_1, 0, color="r")
axes[1, 0].scatter(dist_2, 0, color="b")
axes[1, 0].title.set_text("Electric Field (Volts / m)")
axes[1, 0].set_xlabel("X(m)")
axes[1, 0].set_ylabel("Y(m)")

plt.colorbar(cmap, ax=axes[0, 1], fraction=0.046, pad=0.04)
fig.suptitle("Homework #3")
plt.show()
