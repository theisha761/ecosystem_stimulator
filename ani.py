from abc import ABC,abstractmethod
class Animal(Organism):
    def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy)
        self.__speed=speed
        self.__preylist=prey
    def get_prey(self):
        return self.__preylist
    @abstractmethod
    def eat(self):
        pass
    def hunt(self,a):
        organisms=a.get_organisms()
        for organism in organisms:
            if organism.get_name() in self.__preylist:
                self.eat(organism)
                break
    def __gt__(self,other):
        return self.get_energy()>other.get_energy()
    def __lt__(self,other):
        return self.get_energy()<other.get_energy()
    def __eq__(self,other):
        return self.get_energy()==other.get_energy()
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

        




