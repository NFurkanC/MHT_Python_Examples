import numpy as np
import math

def f_xy(x,y):
    return -1 * x * y ** 3

def fg(x):
    return ((1/(1+x**2)) ** (1/2))

def rk(iter, x0, y0, h):
    print("      iter      x            y               fg              k1             k2")
    for i in range(iter):
        n_i = i
        x_i = x0
        y_i = y0
        f_i = fg(x0)
        k1_i = f_xy(x0, y0)
        x0 = x0 + h
        y0 = y0 + h * k1_i
        k2_i = f_xy(x0, y0)
        y0 = y_i + (h/2) * (k1_i + k2_i)
        print(f"        {i}      {x_i:.4f}       {y_i:.4f}       {fg(x0):.4f}        {k1_i:.4f}      {k2_i:.4f}")

x0 = 0
y0 = 1
h = 0.1
iter = 5
print(rk(iter, x0, y0, h))
