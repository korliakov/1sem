import turtle
import numpy as np


turtle.shape('turtle')

def f(m, n):
    
    for i in range (m*n):
        turtle.forward((i/10)*2*(np.pi)/n)
        turtle.left(360/n)

m = int(input())
n = int(input())
f(m, n)
