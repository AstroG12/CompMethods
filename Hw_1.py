#import
import numpy as np 
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "helvetica"

# array for theta(1a, 2b, 3c) values
theta_1a = np.linspace(0, (2*np.pi), 100)
theta_2b = np.linspace(0, (10*np.pi), 1000)
theta_3c = np.linspace(0, (24*np.pi), 1000)
# eq for problem 1a
x_1a = 2 * np.cos(theta_1a) + np.cos(2 * theta_1a)
y_1a = 2 * np.sin(theta_1a) - np.sin(2 * theta_1a)

# eq for problem 2b
x_2b = (theta_2b**2) * np.cos(theta_2b)
y_2b = (theta_2b**2) * np.sin(theta_2b)

# eq for problem 3c
x_3c = (np.exp(np.cos(theta_3c)) - 2 * np.cos(4 * theta_3c) + ((np.sin(theta_3c))**5) ) * np.cos(theta_3c)
y_3c = (np.exp(np.cos(theta_3c)) - 2 * np.cos(4 * theta_3c) + ((np.sin(theta_3c))**5) ) * np.sin(theta_3c)

# create figures hiding the fourth
fig, ax = plt.subplots(2,2,figsize=(6,6))


ax[1,1].axis("off")

# plot for problem 1a
ax[0,0].plot(x_1a, y_1a, color="red")
ax[0,0].set_title("Problem 1a")
ax[0,0].set_xlabel("X")
ax[0,0].set_ylabel("Y")
#ax[0,0].xaxis.set_label_coords(0.5,-.15)

# plot for problem 2b
ax[0,1].plot(x_2b, y_2b, color="blue")
ax[0,1].set_title("Problem 2b")
ax[0,1].set_xlabel("X")
ax[0,1].set_ylabel("Y")

# plot for problem 3c
ax[1,0].plot(x_3c, y_3c, color="green")
ax[1,0].set_title("Problem 3c")
ax[1,0].set_xlabel("X")
ax[1,0].set_ylabel("Y")

plt.tight_layout()
plt.show()