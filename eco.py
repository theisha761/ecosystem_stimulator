from habi import Habitat
from ani import Animal
class Ecosystem:
    def __init__(self):
        self.__habitatlist=[]
        self.__daycount=0
    def get_habitat(self):
        return self.__habitatlist
    def add_habitat(self,hab):
        self.__habitatlist.append(hab)
    def stimulate(self,days=10):
        for i in range(1,days+1):
            for habitat in self.__habitatlist:
                for organism in habitat.get_org():
                    organism.pass_day()
                    if isinstance(organism,Animal):
                        organism.hunt(habitat)
                habitat.remove_dead()
            print(f''' day number {i} : organisms status: {habitat}''')


 