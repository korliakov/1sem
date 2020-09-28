from random import *
import numpy as np
import turtle


def rand():
    for i in range(100):
        turtle.right(randint(0, 360))
        turtle.forward(randint(0, 100))

rand()
