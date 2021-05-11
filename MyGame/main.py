import pygame
from pygame.locals import *

pygame.init()
width,height = 1000,1000
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("MyGame")

player = pygame.image.load("bunny.jpg")

while 1:
    screen.fill(0)
    screen.blit(player,(100,100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit(0)
