
import scipy.integrate as integrate
from equations import *
from simpson import simpson
from numpy import *
import numpy as np
#Define constants that are used in project

#Neural network configuration paramaters
HIDDEN_NODES = 10
ALPHA = 4.5
LAYERS = 3
#Tan-sigmoid function
def tansig(x):
  x = (x)
  eq = 2/(1+e**(-2*(x)))-1
  return eq

def sin(x):
  return sin(x)

#Linear function
def purelin(x):
    return x

#Leaku RELU
def lRelu(x):
  if x<0:
    return x/10
  else:
    return x  

  
def integration(x, Phi):
  sum = 0
  for k in range(1, 31):
    sum += integrate.quad(lambda t: Phi(x-t) * cos(k*t - ALPHA*pi/2) / (k**ALPHA), 0, 2*pi)[0] \
     # + integrate.quad(lambda t: h(x, t)*Phi(t), 0, pi)[0]
  eq = sum/pi
  return eq 
  
