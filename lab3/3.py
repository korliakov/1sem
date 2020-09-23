import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((2400, 1200))
screen.fill((150, 150, 150))


rect(screen, (0, 128, 0), (0, 600, 2400, 600))
rect(screen, (135, 206, 250), (0, 0, 2400, 600))


def house(x, y, base_length, base_height, window_length, window_height, k):    #Drawing  house
    #x, y - Coordinates  of  top  left  corner  of  the  house
    #base_length, base_height, window_length, window_height - Length  and  height  of  base  and  window
    #k - Constant  that  is  responsible  for  the  scale  of  house
    
    rect(screen, (160, 82, 45), (x, y, base_length*k, base_height*k))    #Base
    rect(screen, (0, 0, 0), (x, y, base_length*k, base_height*k), 1)    
    polygon(screen, (255, 0, 0), [(x, y), (x+base_length*k, y), (x+int(base_length*k/2), y-180), (x, y)])    #Roof
    polygon(screen, (0, 0, 0), [(x, y), (x+base_length*k, y), (x+int(base_length*k/2), y-180), (x, y)], 1)
    rect(screen, (0, 206, 209), (x+int(base_length*k/2)-(window_length*k)//2, y+int(base_height*k/2)-(window_height*k)//2, window_length*k, window_height*k))    #Window  
    rect(screen, (139, 69, 19), (x+int(base_length*k/2)-(window_length*k)//2, y+int(base_height*k/2)-(window_height*k)//2, window_length*k, window_height*k), 3)    
    
def tree(x, y, k):    #Drawing  tree
    #x, y - Coordinates  of  top  left  corner  of  the  tree trunk
    #k - Constant  that  is  responsible  for  the  scale  of  tree
    
    rect(screen, (0, 0, 0), (x, y, 30*k, 150*k))    #Tree  trunk
    circle(screen, (39, 139, 34), (x+15*k, y-51*k-36*k), 45*k)    #1
    circle(screen, (39, 139, 34), (x+15*k+36*k, y-51*k-15*k), 45*k)    #2
    circle(screen, (39, 139, 34), (x+15*k-36*k, y-51*k-15*k), 45*k)    #3
    circle(screen, (39, 139, 34), (x+15*k, y-51*k), 45*k)    #4
    circle(screen, (39, 139, 34), (x+15*k+30*k, y-51*k+24*k), 45*k)    #5
    circle(screen, (39, 139, 34), (x+15*k-30*k, y-51*k+24*k), 45*k)    #6
    
def cloud(x, y, k):    #Drawing  cloud
    #x, y - Coordinates  of  top  left  corner  of  first  circle
    #k - Constant  that  is  responsible  for  the  scale  of  cloud
    
    circle(screen, (250, 250, 250), (x, y), 45*k) 
    circle(screen, (250, 250, 250), (x+40*k, y), 45*k) 
    circle(screen, (250, 250, 250), (x+80*k, y), 45*k) 
    circle(screen, (250, 250, 250), (x+120*k, y), 45*k) 
    circle(screen, (250, 250, 250), (x+80*k, y-40*k), 45*k) 
    circle(screen, (250, 250, 250), (x+40*k, y-40*k), 45*k) 
    
def sun(x, y, radius):    #Drawing sun
    #x, y - Coordinates  of  top  left  corner  of  the  sun  centre
    circle(screen, (255, 182, 193), (x, y), radius) 
    
house(200, 500, 300, 240, 100, 100, 2)    #Left  house
house(1500, 550, 300, 240, 120, 120, 1)    #Right house
sun(200, 130, 75)
tree(1000, 550, 2)    #Left tree
tree(1900, 550, 1)    #Right tree
cloud(400, 200, 2)    #Left  cloud
cloud(1400, 190, 1)    #Mid  cloud
cloud(2000, 250, 2)    #Right  cloud

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()






