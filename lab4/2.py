import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 0.5
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]



def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)    
    vx = randint(-1, 1)
    vy = randint(-1, 1)
    
    color = COLORS[randint(0, 5)]
    r = randint(10,50)
    for i in range(500):
        circle(screen, (0, 0, 0), (x, y), r)
        clock.tick(500*FPS)
        x += vx
        y += vy  
        circle(screen, color, (x, y), r)
        if x == 0 or x == 1200:
            vx = -vx
        if y == 0 or y == 1200:
            vy = -vy
        pygame.display.update()


s = 0

def click(event):
    global s
    if event.type == pygame.MOUSEBUTTONDOWN:
        x0, y0 = event.pos
        if (x-x0)**2+(y-y0)**2 <= r**2:
            s += 1
            circle(screen, (0, 0, 0), (x, y), r)
            pygame.display.update()
            
            
            

pygame.display.update()
clock = pygame.time.Clock()
finished = False

    

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        click(event)
    new_ball()
    
    
    pygame.display.update()
    screen.fill(BLACK)      
print(s)
pygame.quit()







