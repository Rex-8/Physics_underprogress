import pygame

WW,WH = 800,600
win = pygame.display.set_mode((WW,WH))
win.fill((255,255,255))

class Spring:
    def __init__(self,k,mass,pos1,pos2,pos3):
        self.x1,self.y1 = pos1
        self.x2,self.y2 = pos2
        self.tx,self.ty = pos3
        self.vx,self.vy = 0,0
        self.k = -k
        self.m = mass
    
    def get_length(self):self.length = ((self.ty-self.y1)**2+(self.tx-self.x1)**2)**0.5
    
    def display_spring(self):pygame.draw.line(win,(0,0,0),(self.x1,self.y1),(self.tx,self.ty),2)
    
    def calc_force(self):
        dx = self.tx - self.x2
        dy = self.ty - self.y2
        print(dx,dy)
        ax =  self.k * dx / self.m
        self.vx = (self.vx+ax) * 0.99
        self.tx += self.vx * 0.99
        ay =  self.k * dy / self.m
        self.vy = (self.vy+ay) * 0.99
        self.ty += self.vy
        print(ax,ay)
    
    def update_pos(self):
        self.calc_force()
        self.display_spring()

spring1 = Spring(0.01,1,(200,100),(250,300),(200,400))
spring1.display_spring()

clock = pygame.time.Clock()

run = True
while run:
    win.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    spring1.update_pos()
    spring1.display_spring()
    clock.tick(30)
    pygame.display.update()  
pygame.quit()