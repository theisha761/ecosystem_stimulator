from ani import Animal
class Aquatic():
    def swim(self):
        return "swimming"
class Mammal():
    def breathe(self):
        return "breathes"
class AquaticMammal(Animal,Aquatic,Mammal):
    def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
    def reproduce(self):
        return AquaticMammal(self.get_name(),0,10,10,10,self.get_prey())
    def make_sound(self):
        return "hohihohi"
    def eat(self,prey):
        e=prey.get_energy()
        prey.set_is_alive(False)
        prey.set_energy(0)
        f=self.get_energy()
        self.set_energy(f+e)
class Dolphin(AquaticMammal):
    def __init__(self,name,age,health,energy,speed,prey):
        super().__init__(name,age,health,energy,speed,prey)
    def reproduce(self):
        return Dolphin(self.get_name(),0,10,10,10,self.get_prey())
    def make_sound(self):
        return "heeeeeeem"
    

