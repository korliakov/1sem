import turtle
import numpy as np


turtle.shape('turtle')

def f(n):
    
    for i in range (n):
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)
        turtle.right(360/n)
        
        
        

n = int(input())

f(n)
