from numpy import *
import numpy as np
import scipy.integrate as integrate
#Define equations of the examples in the project file

NUMBER = 2 #No. of examples in project

#Right-side equation
def right_eq(x):
    eq = sin(x-pi/4)
    return eq
#Analytical solution
def analytic(x):
    eq = sin(x)
    return eq

def h(x, t):
    eq = x*t
    return eq
