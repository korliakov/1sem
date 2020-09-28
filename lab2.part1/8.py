import turtle
import numpy as np


turtle.shape('turtle')

def f(n):
    
    for i in range (1, n+1):
        turtle.forward(20*i)
        turtle.left(90) 
        turtle.forward(20*i)
        turtle.left(90)
       
        
print('Введите количесвто витков')
n = 2*int(input())

f(n)

