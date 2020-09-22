import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((150, 150, 150))


circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
rect(screen, (0, 0, 0), (155, 250, 90, 20))
circle(screen, (255, 0, 0), (160, 160), 20)
circle(screen, (0, 0, 0), (160, 160), 20, 1)
circle(screen, (255, 0, 0), (240, 160), 15)
circle(screen, (0, 0, 0), (240, 160), 15, 1)
circle(screen, (0, 0, 0), (160, 160), 8)
circle(screen, (0, 0, 0), (240, 160), 8)
polygon(screen, (0, 0, 0), [(100,100), (200,150),
                               (195,155), (95, 105), (100,100)])

polygon(screen, (0, 0, 0), [(220, 150), (280, 110),
                               (280, 115), (220, 155), (220, 150)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()