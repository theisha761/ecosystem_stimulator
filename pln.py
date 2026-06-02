from organm import Organism
class Plant(Organism):
    def __init__(self,name,age,health,energy,height,sunlight):
        super().__init__(name,age,health,energy)
        self.__height=height
        self.__sunlight=sunlight
    def get_height(self):
        return self.__height
    def get_sunlight(self):
        return self.__sunlight
    def set_height(self,h):
        self.__height=h
    def eat(self):
        e=self.get_energy()
        e=e+self.__sunlight
        self.set_energy(e)
    def make_sound(self):
        return "rustle"
    def reproduce(self):
        return Plant(self.get_name(),0,10,10,0.5,self.__sunlight)    
    def grow(self):
        self.__height=self.__height+0.0025
class Tree(Plant):
    def __init__(self,name,age,health,energy,height,sunlight):
        super().__init__(name,age,health,energy,height,sunlight)
    def grow(self):
        s=self.get_height()
        s=s+0.000015
        self.set_height(s)
    def reproduce(self):
        return Tree(self.get_name(),0,10,10,0.5,self.get_sunlight())
    def make_sound(self):
        return "Tree rustle"
class Grass(Plant):
    def __init__(self,name,age,health,energy,height,sunlight):
        super().__init__(name,age,health,energy,height,sunlight)
    def grow(self):
        s=self.get_height()
        s=s+0.025
        self.set_height(s)
    def reproduce(self):
        return Grass(self.get_name(),0,10,10,0.005,self.get_sunlight())
    def make_sound(self):
        return "no sound"

        
