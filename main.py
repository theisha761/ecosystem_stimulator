from habi import Habitat
from pln import Plant,Tree,Grass
from organm import Organism
from ani import Animal,Carnivore,Herbivore,Omnivore,Tiger,Deer,Bear
from eco import Ecosystem
forest=Habitat("forest","tropical")
tree1=Tree("banayan",10,10,10,10,10)
tree2=Tree("Mango",10,10,10,10,10)
grass=Grass("weed",10,10,10,10,10)
tiger=Tiger("tiger",100,50,50,100,["deer","rabbit"])
deer=Deer("deer",20,25,25,50,["grass"])
bear=Bear("bear",40,60,60,45,["banayan","Mango","weed","tiger","deer","bear"])
Eco=Ecosystem()
forest.add_org(tree1)
forest.add_org(tree2)
forest.add_org(grass)
forest.add_org(tiger)
forest.add_org(deer)
forest.add_org(bear)
Eco.add_habitat(forest)
Eco.stimulate()
