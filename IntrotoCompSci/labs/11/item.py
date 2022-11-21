"""
Item Class for Neko Atsume App

Name: Vladimir Soto-Avina
Date: 4/28/2020
"""

from utils import *

class Item(object):
    def __init__(self, name, cost, itype):
        self.name = name
        self.cost = cost
        self.itype = itype

    def __str__(self):
        string = "%s (%s): %d fishes" % (self.name, self.itype, self.cost)
        return string

    def getName(self):
        """returns name of item object"""
        return self.name

    def getCost(self):
        """returns cost of item object"""
        return self.cost

    def getItemType(self):
        """returns type of item object"""
        return self.itype

    def setCost(self, cost):
        """assigns cost of item object using a cost parameter"""
        self.cost = cost

    def isToy(self):
        """returns true or false depending if item object is a toy"""
        if self.itype == "toy":
            return True
        else:
            return False

    def isFood(self):
        """returns true or false depending if item object is a food"""
        if self.itype == "food":
            return True
        else:
            return False



# ------------------------------------------------ #
# Note: below is test code for the Item class.
# You should look at it, but do not need to modify it.

def main():
    """test the item class"""

    items = loadItems("items.txt")   # from utils.py
    for item in items:
        print(item)                  # should just show all items


    # more tests using a fake item and assert statements.
    # info on asserts:  https://www.cs.swarthmore.edu/pyref/#_assert
    # no output from this means your Item class works!
    # if you get an AssertionError, something in your class doesn't work
    # (probably because you haven't written the method yet)

    name = "AnItem"
    cost = 100
    itype = "toy"
    fakeitem = Item(name,cost,itype)
    assert(fakeitem.getName()==name)
    assert(fakeitem.getCost()==cost)
    assert(fakeitem.getItemType()==itype)
    assert(fakeitem.isToy()==True)
    assert(fakeitem.isFood()==False)
    fakeitem.setCost(cost*2)
    assert(fakeitem.getCost()==cost*2)

if __name__ == "__main__":
    main()
