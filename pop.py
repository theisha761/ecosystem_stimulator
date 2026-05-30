class Population:
    def __init__(self,name,count):
        self.name=name
        self.count=count
    def __str__(self):
        return (str(self.name)+":"+str(self.count))
    def __add__(self,other):
        if self.name==other.name:
            s=self.count+other.count
            return Population(self.name,s)
        else:
            raise ValueError("you dont add population of different species")
    def __gt__(self,other):
        return self.count>other.count
    def __lt__(self,other):
        return self.count<other.count
    def __eq__(self,other):
        return self.count==other.count
        
