# imports
import numpy as np
import matplotlib.pyplot as plt


# Thetas for 1a, 2b, 3c

theta_1a = np.linspace(0, 2 * np.pi, 50)
theta_2b = np.linspace(0, 10 * np.pi, 1000)
theta_3c = np.linspace(0, 24 * np.pi, 1500)


# eq for 1a

x_1a = 2 * np.cos(theta_1a) + np.cos(2 * theta_1a)
y_1a = 2 * np.sin(theta_1a) - np.sin(2 * theta_1a)

#eq for 2b

x_2b = (theta_2b**2) * np.cos(theta_2b)
y_2b = (theta_2b**2) * np.sin(theta_2b)

#eq for 3c

x_3c = ((np.exp(np.cos(theta_3c))) - (2 * np.cos(4 * theta_3c)) + (np.sin(theta_3c / 12)**5)) * np.cos(theta_3c)
y_3c = ((np.exp(np.cos(theta_3c))) - (2 * np.cos(4 * theta_3c)) + (np.sin(theta_3c / 12)**5)) * np.sin(theta_3c)


# Plots

fig, axes = plt.subplots(2,2, figsize=(7.5,7.5))
axes[1,1].axis("off")

axes[0,0].plot(x_1a,y_1a,color="r", linewidth=2)
axes[0,0].set_xlabel("X")
axes[0,0].set_ylabel("Y")
axes[0,0].set_title("1a")

axes[0,1].plot(x_2b,y_2b,color="b", linewidth=2)
axes[0,1].set_xlabel("X")
axes[0,1].set_ylabel("Y")
axes[0,1].set_title("2b")

axes[1,0].plot(x_3c,y_3c,color="g", linewidth=2)
axes[1,0].set_xlabel("X")
axes[1,0].set_ylabel("Y")
axes[1,0].set_title("3c")

plt.rcParams["font.family"] = "helvetica"
fig.tight_layout()
plt.show()
