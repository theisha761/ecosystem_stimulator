from habi import Habitat
from ani import Animal
from organm import Organism
from pln import Plant
class Ecosystem:
    def __init__(self):
        self.__habitatlist=[]
        self.__daycount=0
    def get_habitat(self):
        return self.__habitatlist
    def add_habitat(self,hab):
        self.__habitatlist.append(hab)
    def simulate(self,days=10):
        for i in range(1,days+1):
            for habitat in self.__habitatlist:
                for organism in habitat.get_org():
                    organism.pass_day()
                    if isinstance(organism,Animal):
                        organism.hunt(habitat)
                    if isinstance(organism, Plant):
                        organism.grow()
                        organism.eat()
                habitat.remove_dead()
                count={}
                for o in habitat.get_org():
                    species=o.__class__.__name__
                    if species in count:
                        count[species]=count[species]+1
                    else:
                        count[species]=1
                
                print(f''' day number {i} : organisms status: {habitat}\n
                {count}''')


 