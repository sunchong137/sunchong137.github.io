'''
Reverse mode automatic differentiation. 
Example:
    f = x1*x2 + sin(x1) 
'''
import numpy as np

class re_var():
    # the data structure for reverse mode
    def __init__(self, v=1, children=[]):
        self.val = v # value of the variable
        self.children = children # list of tuples (coeff, re_var) 
        self.grad = 0 # gradient


def f_add(x, y):
    # x + y
    var = re_var()
    var.val = x.val + y.val
    var.children = [(1, x), (1, y)] # child x with coefficient 1, and y with 1
    return var 

def f_prod(x, y):
    # x * y
    var = re_var()
    var.val = x.val * y.val
    var.children = [(y.val, x), (x.val, y)] 
    return var

def f_sin(x):
    # sin(x)
    var = re_var()
    var.val = np.sin(x.val) 
    var.children = [(np.cos(x.val), x)]
    return var


def calc_grad(var, acc_grad=1):
    # var: the unit at the top hierarchy
    # acc_grad: accumulated gradient from parents
    # evaluate the gradient recursively, so every unit has a gradient
    var.grad += acc_grad 
    for coef, child in var.children:
        calc_grad(child, coef * acc_grad)


def func(x1, x2):
    return f_add(f_prod(x1, x2), f_sin(x1))

# define x1 and x2
x1 = re_var(0)
x2 = re_var(1)
var = func(x1, x2)

calc_grad(var)

print("value: ", var.val)
print("gradient wrt x1: ", x1.grad)
print("gradient wrt x2: ", x2.grad)
