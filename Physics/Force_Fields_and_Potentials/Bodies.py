from Vectors import vector
import pygame

G = 6.6743 * 10**-11
k = 9 * 10**9

class Object:
    def __init__(self,environment,mass,size,charge,pos,vel,acc):
        self.mass = mass
        self.size = size
        self.charge = charge
        self.environment = environment
        environment.bodies.append(self)
        self.pos = vector(pos)
        self.vel = vector(vel)
        self.acc = vector(acc)
        self.posx,self.posy,self.posz = pos
        self.velx,self.vely,self.velz = vel
        self.accx,self.accy,self.accz = acc
    
    def get_grav_field(self,position):       # Grav field due to self
        position = vector(position)
        dist = position.subtract(self.pos)
        try:
            field = dist.vect_form(G*self.mass/dist.magn**2)
        except:
            field = vector((0,0,0))
        return field
    
    def get_grav_potential(self,position):
        dist = position.subtract(self.pos)
        return self.get_grav_field(self,position).s_prod(dist)

    def get_electric_field(self,position):       # Grav field due to self
        position = vector(position)
        dist = position.subtract(self.pos)
        field = dist.vect_form(k*self.charge/dist.magn**2)
        return field
    
    def get_electric_potential(self,position):
        dist = position.subtract(self.pos)
        return self.get_grav_potential(self,position).s_prod(dist)

    def display(self):
        pygame.draw.circle(self.environment.window,(0,0,0),(self.posx,self.posy),self.size)