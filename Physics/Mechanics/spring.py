import pygame

WW, WH = 800, 600
win = pygame.display.set_mode((WW, WH))
win.fill((255, 255, 255))

class Spring:
    def __init__(self, k, mass, pos1, pos2, pos3):
        self.x1, self.y1 = pos1
        self.x2, self.y2 = pos2
        self.tx, self.ty = pos3
        self.k = -k
        self.m = mass
        self.vx, self.vy = 0, 0  # Introduce velocity

    def calc_force(self):
        dx = self.tx - self.x2
        dy = self.ty - self.y2
        ax = self.k * dx / self.m
        ay = self.k * dy / self.m

        self.vx = 0.99 * (self.vx + ax)
        self.vy = 0.99 * (self.vy + ay)

        self.tx += self.vx
        self.ty += self.vy

    def display_spring(self):
        pygame.draw.line(win, (0, 0, 0), (self.x1, self.y1), (self.tx, self.ty), 2)

    def update_pos(self):
        self.calc_force()
        self.display_spring()

spring1 = Spring(0.01, 1, (200, 100), (200, 300), (200, 400))
spring1.display_spring()

clock = pygame.time.Clock()
run = True

while run:
    win.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    spring1.update_pos()
    pygame.display.update()
    clock.tick(30)

pygame.quit()
