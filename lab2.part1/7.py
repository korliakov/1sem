import turtle
import numpy as np


turtle.shape('turtle')

def f(m, n):
    
    for i in range (m*n):
        turtle.forward((i/10)*2*(np.pi)/n)    #n  отвечает  за  "точность  и  угловатость"  прорисовки
        turtle.left(360/n)
print('Введите количество витков')
m = int(input())
print('Введите параметр точности (рекомендуется 100)')
n = int(input())
f(m, n)
