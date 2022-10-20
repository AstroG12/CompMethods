import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct

dow = np.loadtxt("dow.txt", float)
dow2 = np.loadtxt("dow2.txt", float)

# Part 1
plt.plot(dow, "r", label="dow")
c = np.fft.fft(dow)
d = c.copy()
for i in range(len(c)):
    if i > len(c) * 0.1:
        c[i] = 0
for i in range(len(d)):
    if i > len(d) * 0.02:
        d[i] = 0
inv_fc = np.fft.ifft(c)
inv_fd = np.fft.ifft(d)
plt.plot(inv_fc, "b", label="10%")
plt.plot(inv_fd, "g", label="2%")

# Part 2
e = np.fft.fft(dow2)
for i in range(len(e)):
    if i > len(e) * 0.02:
        e[i] = 0
f = dct(dow2)
for i in range(len(f)):
    if i > len(f) * 0.02:
        f[i] = 0

inv_fe = np.fft.ifft(e)
inv_ff = idct(f)
# plt.plot(dow2,"b")
# plt.plot(inv_fe, "r")
# plt.plot(inv_ff, "g")
plt.legend()
plt.show()
