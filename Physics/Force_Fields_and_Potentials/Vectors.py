class vector():
    def __init__(self,coord):
        self.coord = coord
        self.x = coord[0]
        self.y = coord[1]
        self.z = coord[2]
        self.magn = ((self.x**2)+(self.y**2)+(self.z**2))**0.5

    def printV(self):print((self.x,self.y,self.z))

    def add(self,other):return vector((self.x+other.x,self.y+other.y,self.z+other.z))
    def subtract(self,other):return self.add(other.negative())
    
    def s_prod(self,other):return vector((self.x*other,self.y*other,self.z*other))
    def d_prod(self,other):return float((self.x*other.x)+(self.y*other.y)+(self.z*other.z))
    def c_prod(self,other):return vector(((self.y*other.z-self.z*other.y),-(self.x*other.z-other.x*self.z),(self.x*other.y-self.y*other.x)))
    
    def vect_form(self,other):return vector(((other*self.x/self.magn),(other*self.y/self.magn),(other*self.z/self.magn)))
    
    def negative(self):return vector((-self.x,-self.y,-self.z))