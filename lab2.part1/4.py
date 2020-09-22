import turtle
import numpy as np


turtle.shape('turtle')


n = 100
for i in range (n):
    turtle.forward(100*2*(np.pi)/n)
    turtle.left(360/n)
