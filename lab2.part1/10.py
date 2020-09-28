import turtle
import numpy as np


turtle.shape('turtle')


def f():

    n = 100
    for i in range (n):
        turtle.forward(50*2*(np.pi)/n)
        turtle.left(360/n)

print('Введите количество лепестков')
k = int(input())

def flower(k):
    
    
    for i in range(k):
        f()
        turtle.left(360/k)
    
    
    
flower(k)
