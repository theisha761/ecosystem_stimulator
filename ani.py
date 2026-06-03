from abc import ABC,abstractmethod
from organm import Organism
from pln import Plant
class Animal(Organism):
    def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy)
        self.__speed=speed
        self.__preylist=prey
    def get_prey(self):
        return self.__preylist
    def get_speed(self):
        return self.__speed
    @abstractmethod
    def eat(self):
        pass
    def hunt(self,a):
        organisms=a.get_org()
        for organism in organisms:
            if organism.get_name() in self.__preylist:
                if isinstance(organism,Animal):
                    if self.get_speed()>organism.get_speed():
                        self.eat(organism)
                    else:
                        print(f'''{organism.get_name()} escaped from {self.get_name()}''')
                else:
                    self.eat(organism)

                break

class Herbivore(Animal):
    def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
    def eat(self,plant):
        e=plant.get_energy()
        plant.set_energy(0)
        f=self.get_energy()
        self.set_energy(f+e)
    def reproduce(self):
        return Herbivore(self.get_name(),0,10,10,100,self.get_prey())
    def make_sound(self):
        return "mow"
class Deer(Herbivore):
     def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
     def reproduce(self):
        return Deer(self.get_name(),0,10,10,100,self.get_prey())
     def make_sound(self):
        return "vee"
class Rabbit(Herbivore):
     def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
     def reproduce(self):
        return Rabbit(self.get_name(),0,10,10,100,self.get_prey())
     def make_sound(self):
        return "hummm"
class Carnivore(Animal):
    def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
    def eat(self,prey):
        e=prey.get_energy()
        prey.set_is_alive(False)
        prey.set_energy(0)
        f=self.get_energy()
        self.set_energy(f+e)
    def reproduce(self):
        return Carnivore(self.get_name(),0,10,10,100,self.get_prey())
    def make_sound(self):
        return "hoow"
class Tiger(Carnivore):
     def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
     def reproduce(self):
        return Tiger(self.get_name(),0,10,10,100,self.get_prey())
     def make_sound(self):
        return "aaahu"
class Snake(Carnivore):
     def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
     def reproduce(self):
        return Snake(self.get_name(),0,10,10,100,self.get_prey())
     def make_sound(self):
        return "siiish"
class Omnivore(Animal):
    def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
    def eat(self,prey):
        if isinstance(prey,Plant):
            e=prey.get_energy()
            prey.set_energy(0)
            f=self.get_energy()
            self.set_energy(f+e)
        else:
            e=prey.get_energy()
            prey.set_is_alive(False)
            prey.set_energy(0)
            f=self.get_energy()
            self.set_energy(f+e)
    def reproduce(self):
        return Omnivore(self.get_name(),0,10,10,100,self.get_prey())
    def make_sound(self):
        return "ohhh"
class Bear(Omnivore):
     def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
     def reproduce(self):
        return Bear(self.get_name(),0,10,10,100,self.get_prey())
     def make_sound(self):
        return "haaaul"
class Fish(Animal):
    def __init__(self, name, age, health, energy, speed, prey):
        super().__init__(name, age, health, energy, speed, prey)
    def eat(self, prey):
        e = prey.get_energy()
        prey.set_energy(0)
        f = self.get_energy()
        self.set_energy(f + e)
    def reproduce(self):
        return Fish(self.get_name(), 0, 10, 10, 30, self.get_prey())
    def make_sound(self):
        return "..."
        




