import numpy as np

def sum_squared_error_function(y, t):
    return 0.5 * np.sum((y-t)**2)