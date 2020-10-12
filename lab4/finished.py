import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30

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
    '''рисует новый шарик '''
    
    
    global Balls
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(70, 100)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    
    Balls.append([x, y, vx, vy, r, color])
    
    


def click_check(event, number):
    global score, Balls
    flag = True
    Ball = Balls[number]
    if (Ball[0] - event[0])**2 + (Ball[1] - event[1])**2 <= Ball[4]**2:
        score += 1
    else:
        flag = not flag
    return flag




def move_balls():
    global Balls, score
    screen.fill((0, 0, 0))
    for number in range(len(Balls)):
        Ball = Balls[number]
        circle(screen, Ball[5], (Ball[0], Ball[1]), Ball[4])
        if Ball[0] <= Ball[4] or Ball[0] >= 1200 - Ball[4]:
            Ball[2] = -Ball[2]
        if Ball[1] <= Ball[4] or Ball[1] >= 900 - Ball[4]:
            Ball[3] = -Ball[3]
        Ball[0] += Ball[2]
        Ball[1] += Ball[3]
    
    pygame.display.update()     

pygame.display.update()
clock = pygame.time.Clock()
finished = False


Balls = []
score = 0 

for i in range(10):
    new_ball()
move_balls()
pygame.display.update()   
while not finished:
    clock.tick(FPS)
    move_balls()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            state = False
            for number in range(len(Balls)):
                if click_check(event.pos, number):
                    del(Balls[number])
                    new_ball()
                    state = True
            if state:
                print('Sniper! Your score: ', score)
            else:
                print('You have missed! Loooser ')
            move_balls()
            
            
            
            
    
    

    
print('Your final result: ', score)
pygame.quit()
