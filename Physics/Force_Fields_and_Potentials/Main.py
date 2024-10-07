from Vectors import *
from Bodies import *
from Environments import *
import pygame

win = pygame.display.set_mode((400,400))
window = Environment(win,(192,192,192))

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            window.bodies.append(Object(window,1000,20,0,tuple(pos+(0,)),(0,0,0),(0,0,0)))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                pos = pygame.mouse.get_pos()
                window.net_grav_field(tuple(pos+(0,))).printV()
                
    window.display()
    pygame.display.update()
pygame.quit()