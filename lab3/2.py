import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 400))
screen.fill((150, 150, 150))


rect(screen, (0, 128, 0), (0, 200, 800, 200))
rect(screen, (135, 206, 250), (0, 0, 800, 200))


def house():
    rect(screen, (160, 82, 45), (x, y, 160, 160))
    rect(screen, (0, 0, 0), (x, y, 160, 160), 1)
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()