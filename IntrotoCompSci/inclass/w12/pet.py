"""
Define a new class to represent pets
"""

class Pet(object):
    def __init__(self, name, animal):
    self.name = name
    self.animal = animal
    self.toys = toys

    def __str__(self):
        #this special method creates a string representation of the object
        string = "%s: %s" % (self.animal, self.name)
        if len(self.toys) > 0:
            string = string + " Toys: "
            for i in range(len(self.toys)):
                string = string + self.toys[i] + " "


    def getName(self):
        #an example of a getter
        return self.name

    def getAnimalType(self):
        return self.animal_type

    def setName(self, new_name):
        self.name = new_name

    def addToy(self, toy):
        self.toys.append(toy)


def main():
    cat1 = Pet("Scout", "cat")    #this calls the constructor!
    cat2 = Pet("Pumpkin", "cat")
    dog = Pet("Cosmo", "dog")
    print(cat1) #this calls the str method
    cat1.addToy("shoe string")
    cat1.addToy("furry mouse")


main()
