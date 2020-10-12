import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1

screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

Ball = []
def new_ball():
    '''рисует новый шарик '''
    
    
    global N, Ball
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(70, 100)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    
    Ball.append([x, y, vx, vy, r, color])
    k = len(Ball)
    circle(screen, Ball[k-1][5], (Ball[k-1][0], Ball[k-1][1]), Ball[k-1][4])
    

s = 0
def click_ball(event):
    global s, Ball
    if event.type == pygame.MOUSEBUTTONDOWN:
        x0, y0 = event.pos
        for i in range(len(Ball)):
            if (Ball[i][0]-x0)**2+(Ball[i][1]-y0)**2 <= Ball[i][4]**2:
                s += 1
                circle(screen, (0, 0, 0), (Ball[i][0], Ball[i][1]), Ball[i][4])
                


def move_ball():
    global Ball
    clock.tick(500*FPS)
    for j in range(500):
        for i in range(len(Ball)):
            circle(screen, (0, 0, 0), (Ball[i-1][0], Ball[i-1][1]), Ball[i-1][4])
            Ball[i-1][0] += Ball[i-1][2]
            Ball[i-1][1] += Ball[i-1][3]
            
            circle(screen, Ball[i-1][5], (Ball[i-1][0], Ball[i-1][1]), Ball[i-1][4])
            pygame.display.update()

    

pygame.display.update()
clock = pygame.time.Clock()
finished = False



while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        
        new_ball()
        
        click_ball(event)
    
    
    pygame.display.update()
    
print(s)
pygame.quit()
