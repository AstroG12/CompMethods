import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct


def fft10(file):
    f = np.loadtxt(file)
    coef = np.fft.fft(f)
    plt.plot(f, "r", label="{}".format(file))
    for i in range(len(coef)):
        if i > len(coef) * 0.1:
            coef[i] = 0
    inv = np.fft.ifft(coef)
    plt.plot(inv, "b", label="10%")
    plt.legend()
    plt.show()


def fft2(file):
    f = np.loadtxt(file)
    coef = np.fft.fft(f)
    plt.plot(f, "r", label="{}".format(file))
    for i in range(len(coef)):
        if i > len(coef) * 0.02:
            coef[i] = 0
    inv = np.fft.ifft(coef)
    plt.plot(inv, "b", label="2%")
    plt.legend()
    plt.show()


def fft210(file):
    f = np.loadtxt(file)
    coef = np.fft.fft(f)
    b = np.copy(coef)
    plt.plot(f, "r", label="{}".format(file))
    for i in range(len(coef)):
        if i > len(coef) * 0.02:
            coef[i] = 0
    for i in range(len(b)):
        if i > len(b) * 0.1:
            b[i] = 0
    inv_a = np.fft.ifft(coef)
    inv_b = np.fft.ifft(b)
    plt.plot(inv_a, "b", label="2%")
    plt.plot(inv_b, "g", label="10%")
    plt.legend()
    plt.show()


def cos2(file):
    f = np.loadtxt(file)
    coef = dct(f)
    plt.plot(f, "r", label="{}".format(file))
    for i in range(len(coef)):
        if i > len(coef) * 0.02:
            coef[i] = 0
    inv = idct(coef)
    plt.plot(inv, "b", label="2% with dct")
    plt.legend()
    plt.show()


def cos2vfft2(file):
    f = np.loadtxt(file)
    coef_fft = np.fft.fft(f)
    coef_cos = dct(f)
    plt.plot(f, "r", label="{}".format(file))
    for i in range(len(coef_cos)):
        if i > len(coef_cos) * 0.02:
            coef_cos[i] = 0
    for i in range(len(coef_fft)):
        if i > len(coef_fft) * 0.02:
            coef_fft[i] = 0
    inv_fft = np.fft.ifft(coef_fft)
    inv_cos = idct(coef_cos)
    plt.plot(inv_fft, "b", label="fft")
    plt.plot(inv_cos, "g", label="cos")
    plt.legend()
    plt.show()


func_map = {"fft10": fft10, "fft2": fft2,
            "fft210": fft210, "cos2": cos2, "cos2vfft2": cos2vfft2}

parser = argparse.ArgumentParser()
# parser.add_argument("file", type=argparse.FileType("r"), nargs="+")
parser.add_argument("file", type=str)
parser.add_argument("command", choices=func_map.keys())

args = parser.parse_args()
func = func_map[args.command]
file = args.file
func(file)
