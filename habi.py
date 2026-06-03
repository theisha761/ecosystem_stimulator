class Habitat:
    def __init__(self,name,climate):
        self.__name=name
        self.__climate=climate
        self.__organisms=[]
    def get_org(self):
        return self.__organisms
    def get_name(self):
        return self.__name
    def get_climate(self):
        return self.__climate
    def add_org(self,org):
        self.__organisms.append(org)
    def remove_dead(self):
        g=self.get_org()
        new_organisms=[]
        for i in g:
            if i.get_is_alive()==True:
                new_organisms.append(i)
        self.__organisms=new_organisms
    def __len__(self):
        return len(self.__organisms)
    def __str__(self):
        result = f"Habitat: {self.__name}\n"
        for org in self.__organisms:
            result =result+ str(org) + "\n"
        return result

        
