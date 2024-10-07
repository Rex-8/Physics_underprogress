from Vectors import vector
import pygame

G = 6.6743 * 10**-11
k = 9 * 10**9

class Environment:
    def __init__(self,win,bg):
        self.bodies = []
        self.window = win
        self.bg = bg
        
    def net_grav_field(self,position):
        field = vector((0,0,0))
        for body in self.bodies:
            field = field.add(body.get_grav_field(position))
        return field
    
    def net_grav_potential(self,position):
        potential = vector((0,0,0))
        for body in self.bodies:
            potential.add(body.get_grav_potential(position))
        return potential
    
    def net_electric_field(self,position):
        field = vector((0,0,0))
        for body in self.bodies:
            field.add(body.get_electric_field(position))
        return field
    
    def net_electric_potential(self,position):
        potential = vector((0,0,0))
        for body in self.bodies:
            potential.add(body.get_electric_potential(position))
        return potential
    
    def display_graph(self):
        self.window.fill(self.bg)
        for x in range(0,400,10):
            pygame.draw.line(self.window,(128,128,128),(x,0),(x,400),1)
        for y in range(0,400,10):
            pygame.draw.line(self.window,(128,128,128),(0,y),(400,y),1)
        
    def display(self):
        self.window.fill(self.bg)
        self.display_graph()
        for l in self.bodies:
            l.display()