import turtle
import numpy as np


turtle.shape('turtle')

def f(n):
    
    for i in range (1, n+1):
        turtle.forward(20*i)
        turtle.left(90) 
        turtle.forward(20*i)
        turtle.left(90)
       
        

n = int(input())

f(n)

