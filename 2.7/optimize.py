
from scipy import optimize
import numpy as np
def f(x):
    return -np.exp(-(x-0.7)**2)
result = optimize.minimize_scalar(f)
result.success #check if solver was successful
x_min = result.x
