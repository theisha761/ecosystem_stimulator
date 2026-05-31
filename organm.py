from abc import ABC, abstractmethod
class Organism(ABC):
    total_organisms=0
    def __init__(self,name,age,health,energy):
        self.__name=name
        self.__age=age
        self.__health=health
        self.__energy=energy
        self.__is_alive=True
        Organism.total_organisms=Organism.total_organisms+1
    def get_health(self):
        return self.__health
    def set_health(self,h):
        if isinstance(h,(int,float)):
            self.__health=h
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_alive(self):
        return self.__is_alive  
    def get_energy(self):
        return self.__energy
    def set_energy(self,h):
        if isinstance(h,(int,float)):
            self.__energy=h
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def reproduce(self):
        pass
    @abstractmethod
    def make_sound(self):
        pass

    def pass_day(self):
        self.__age=self.__age+1
        self.__health=self.__health-0.25
    def __str__(self):
        summ=f'''organism {self.__name} is of age {self.__age} with health {self.__health} and energy {self.__energy} and the fact that it is alive is {self.__is_alive}'''
        return summ


        

    
