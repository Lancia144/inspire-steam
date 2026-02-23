#  Nmae : Daniel nduati
# Date : 23/02/2026
# Program to show inheritance in python

class Animal:
    def __init__(self,  species, weight, food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weight {weight} kg")

    def eat(self,food):
        print(f"the animal eats {food}")

class dog(Animal):
    def __init__(self,color, bark, breed, weight):
        super().__init__(breed, weight, "meat")
        self.breed = breed
        self.color = color
        self.bark = bark

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weight {weight} kg")

    def bark(self, woof):
        print(f"The dog barks {woof}")

class  Horse(Animal):
    def __init__(self,species, height):
        super().__init__(species, weight, food)
        self.height = height
        self.species = species

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weight {weight} kg")

    def neigh(self,neigh):
        print(f"the horse neighs {neigh}")
