'''
Forward-mode automatic differentiation.
Example:
    y = x1*x2 + sin(x1) 

'''
import numpy as np

class fw_var():
    # define a new data structure to store both value and gradient
    def __init__(self, v=0, g=1):
        self.val = v # value
        self.grad = g # gradient

def f_prod(x, y):
    # evaluate x * y
    var = fw_var()
    var.val = x.val * y.val
    var.grad = x.val * y.grad + x.grad * y.val
    return var 

def f_add(x, y):
    # evaluate x + y
    var = fw_var()
    var.val = x.val + y.val 
    var.grad = x.grad + y.grad 
    return var

def f_sin(x):
    # evaluate sin(x)
    var = fw_var()
    var.val = np.sin(x.val)
    var.grad = np.cos(x.val) * x.grad 
    return var


def func(x1, x2):
    # The function to be evaluated 
    # f = x1*x2 + sin(x1) 
    return f_add(f_prod(x1, x2), f_sin(x1))

x1 = fw_var(0, 1)
x2 = fw_var(1, 0)

var = func(x1, x2)
print(f"Value of f: {var.val}")
print(f"Grad wrt x1: {var.grad}")






