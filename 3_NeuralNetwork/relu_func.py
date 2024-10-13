import numpy as np
import matplotlib.pylab as plt


def relu_func(x):
    return np.where(x > 0, x, 0)

def relu_func_simple(x):
    return np.maximum(0, x)