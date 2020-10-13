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
    r = randint(40, 100)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    
    Balls.append([x, y, vx, vy, r, color])
    
    

def new_square():
    '''рисует новый квадратик '''
    global Squares
    x = randint(100, 1100)
    y = randint(100, 900)
    a = randint(30, 70)
    
    vx = [-10, -9, -8, -7, 10, 9, 8, 7]
    vy = [-10, -9, -8, -7, 10, 9, 8, 7]
    color = COLORS[randint(0, 5)]
    
    Squares.append([x+int(a/2), y+int(a/2), vx[randint(0, 7)], vy[(randint(0, 7))], a, color])
    
    


def move_balls_and_squares():
    global Balls, score, Squares
    screen.fill((50, 199, 199))
    for number in range(len(Balls)):
        Ball = Balls[number]
        circle(screen, Ball[5], (Ball[0], Ball[1]), Ball[4])
        #circle(screen, (0, 0, 0), (Ball[0], Ball[1]), Ball[4], 1)    #Выглядит стремненько
        if Ball[0] <= Ball[4] or Ball[0] >= 1200 - Ball[4]:
            Ball[2] = -Ball[2]
        if Ball[1] <= Ball[4] or Ball[1] >= 900 - Ball[4]:
            Ball[3] = -Ball[3]
        Ball[0] += Ball[2]
        Ball[1] += Ball[3]
        
        
    for number in range(len(Squares)):
        Square = Squares[number]
        x0 = Square[0] - int(Square[4]/2)
        y0 = Square[1] - int(Square[4]/2)
        rect(screen, Square[5], (x0, y0, Square[4], Square[4]))
        #rect(screen, (0, 0, 0), (x0, y0, Square[4], Square[4]), 1)    #Выглядит стремненько
        if Square[0] <= int(Square[4]/2) or Square[0] >= 1200 - int(Square[4]/2):
            Square[2] = -Square[2]
        if Square[1] <= int(Square[4]/2) or Square[1] >= 900 - int(Square[4]/2):
            Square[3] = -Square[3]
        Square[0] += Square[2]
        Square[1] += Square[3]
        
    pygame.display.update()     

        
def click_check_Ball(event, number):
    global score, Balls
    flag = True
    Ball = Balls[number]
    if (Ball[0] - event[0])**2 + (Ball[1] - event[1])**2 <= Ball[4]**2:
        score += 1
    else:
        flag = not flag
    return flag
    
    
    
def click_check_Square(event, number):
    global score, Squares
    flag = True
    Square = Squares[number]
    if abs(Square[0]-event[0]) <= int(Square[4]/2) and abs(Square[1]-event[1]) <= int(Square[4]/2):
        score += 2
    else:
        flag = not flag
    return flag
    
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False


Balls = []
Squares = []
score = 0 


print('Enter the number of balls')
Balls_num = int(input())
for i in range(Balls_num):
    new_ball()

print('Enter the number of squares')
Squares_num = int(input())
for i in range(Squares_num):
    new_square()

move_balls_and_squares()
pygame.display.update()   
while not finished:
    clock.tick(FPS)
    move_balls_and_squares()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            state = False
            for number in range(len(Balls)):
                if click_check_Ball(event.pos, number):
                    del(Balls[number])
                    new_ball()
                    state = True
            for number in range(len(Squares)):
                if click_check_Square(event.pos, number):
                    del(Squares[number])
                    new_square()
                    state = True
            if state:
                print('Sniper! Your score: ', score)
            else:
                print('You have missed! Loooser ')
            move_balls_and_squares()
            
            
            
            
    
    

    
print('Your final result: ', score)
pygame.quit()
