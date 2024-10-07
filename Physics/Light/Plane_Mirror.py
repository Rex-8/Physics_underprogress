import pygame

win = pygame.display.set_mode((800,600))
win.fill((255,255,255))

pos1,pos2 = (200,250),(200,550)

pygame.draw.line(win,(0,0,0),pos1,pos2,3)
try:
    slope_m = (pos2[1]-pos1[1])/(pos2[0]-pos1[0])
except:
    slope_m = 10**14
Eqn_m = (slope_m,-1,(pos2[1]-(slope_m*pos2[0])))

pos3,pos4 = (400,300),(200,400)
pygame.draw.line(win,(128,128,128),pos3,pos4,1)
try:
    slope_m = (pos4[1]-pos3[1])/(pos4[0]-pos3[0])
except:
    slope_m = 10**14
Eqn_m = (slope_m,-1,(pos2[1]-(slope_m*pos2[0])))

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()