from random import *
import numpy as np
import turtle





x = float(input())
y = float(input())
Vx = float(input())
Vy = float(input())
dt = 0.1
ay = float(input())

turtle.penup()
turtle.goto(x,y)
turtle.pendown()
for i in range(1000):
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    turtle.goto(x,y)
    if y <= 0:
        Vy = -Vy
