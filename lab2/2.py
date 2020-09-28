from random import *
import numpy as np
import turtle



def one():
    
    
    turtle.left(90)
    turtle.forward(20)
    turtle.left(135)
    turtle.forward(10*(2**0.5))
    turtle.penup()
    turtle.left(45)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    


def four():
    
    turtle.left(90)
    turtle.forward(20)
    turtle.backward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.backward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    
    
def seven():
    turtle.penup()
    turtle.backward(10)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(10)
    turtle.right(45)
    turtle.forward(10*(2**0.5))
    turtle.left(135)
    turtle.forward(10)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    


def zero():
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    
    
A = [0]*6
n = '141700' 
for i in range(6):
    A[i] = int(n[i])
    
    
    
    

def draw(i):
    if A[i] == 0:
        zero()
    elif A[i] == 1:
        one()
    elif A[i] == 4:
        four()
    elif A[i] == 7:
        seven()
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()        
        
for j in range(6):
    draw(j)
   
