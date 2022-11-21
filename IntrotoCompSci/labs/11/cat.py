"""
Cat Class for Neko Atsume App

Name: Vladimir Soto-Avina
Date: 4/29/2020
"""

from random import randrange
from utils import *

class Cat(object):
    """cat class  defines cat objects"""
    def __init__(self,name,description,personality):
            """constructor for cat objects"""
        self.name = name
        self.description = description
        self.personality = personality
        self.visits = 0

    def __str__(self):
        """ returns string representaton of cat object"""
        string = "Name: %s\nDescription: %s\nPersonality: %s " % (self.name,
                                            self.description, self.personality)
        return string

    def getName(self):
        """returns name of cat object"""
        return self.name

    def getDescription(self):
        """returns description of cat object"""
        return self.description

    def getPersonality(self):
        """returns personality of cat object"""
        return self.personality

    def getVisits(self):
        """returns visits of cat object"""
        return self.visits

    def getFishes(self):
        """returns a random values for fishes"""
        return randrange(10,51)

    def visited(self):
        """constructor for amount of visits"""
        self.visits += 1













# ------------------------------------------------ #
# Note: below is test code for the Cat class.
# You should look at it, but do not need to modify it.

def main():
    """test the cat class"""
    cats = loadCats("cats.txt")     # from utils.py
    for cat in cats:
        print(cat)                  # should print out all cat objs


    # more tests using a fake cat and assert statements.
    # info on asserts:  https://www.cs.swarthmore.edu/pyref/#_assert
    # no output from this means your Cat class works!
    # if you get an AssertionError, something in your class doesn't work
    # (probably because you haven't written the method yet)

    name = "ACat"
    desc = "Black"
    pers = "Nice"
    fakecat = Cat(name,desc,pers)
    assert(fakecat.getName()==name)
    assert(fakecat.getDescription()==desc)
    assert(fakecat.getPersonality()==pers)
    fishes = fakecat.getFishes()
    assert(fishes>=10 and fishes<=50)
    assert(fakecat.getVisits()==0)
    Nvisits = 5
    for i in range(Nvisits):
        fakecat.visited()
        assert(fakecat.getVisits()==i+1)

if __name__ == "__main__":
    main()
