from matplotlib import pyplot as plt
import numpy as np
 
def f(c,z):
    return z ** 2 + c

def diverge(c, z = 0, n_iter = 20, B = 20000):  # B = boundry / limit
    c = complex(*c)
    for i in range(n_iter):
        z = f(c,z)
    if(abs(z) > B): return 1
    else: return 0

res = 200
xmin, xmax = -2,1
ymin, ymax = -1,1
xx, yy = np.meshgrid(np.linspace(xmin, xmax, res), np.linspace(ymin, ymax, res))

#print(xx.shape, yy.shape)
points = np.c_[xx.ravel(), yy.ravel()]

print([diverge(c) for c in points])
