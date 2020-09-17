from random import randint
import turtle
import numpy as np


number_of_turtles = 30
steps_of_time_number = 1000


pool = [turtle.Turtle() for i in range(number_of_turtles)]
Vx = [randint(-50, 50) for i in range(number_of_turtles)]
Vy = [randint(-50, 50) for i in range(number_of_turtles)]
x = [randint(-400, 400) for i in range(number_of_turtles)]
y = [randint(-400, 400) for i in range(number_of_turtles)]
for i in range(number_of_turtles):
    pool[i].penup()
    
dt = 0.2

for j in range(steps_of_time_number):
    for i in range(number_of_turtles):
        x[i] += Vx[i]*dt
        y[i] += Vy[i]*dt
        pool[i].goto(x[i], y[i])
        if np.abs(x[i]) > 400:
            Vx[i] *= -1
        if np.abs(y[i]) > 400:
            Vy[i] *= -1
