"""
Store Class for Neko Atsume App

CS21
Spring 2020
"""

from utils import *
from random import randrange
from copy import copy

class Store(object):
    """store class...defines cat store objects"""

    def __init__(self,items=[]):
        """constructor for store objects"""
        self.items = []     # the items in the store
        for item in items:
           self.addItem(item)

    def __str__(self):
        """return string representation of store obj"""
        s = "Store Inventory: \n"
        for i in range(len(self.items)):
            s += "%2d. %18s (%4s) $%3d fishes\n" % (i+1,
                    self.items[i].getName(), self.items[i].getItemType(),
                    self.items[i].getCost())
        return s

    def getNumItems(self):
        """return number of unique items in store"""
        return len(self.items)

    def addItem(self,item):
        """add given item to the store"""
        self.items.append(item)

    def getItemCost(self, number):
        """check/get cost of an item, given item number (ex 1,2,3...)"""
        index = number - 1
        if index >= 0 and index < len(self.items):
            cost = self.items[index].getCost()
            return cost
        else:
            print("I don't think we have that item...")
            return 0

    def buyItem(self, number):
        """
        given an item number (ex 1,2,3..), 'sell' that item to the customer.
        this method will return the item object if available, and return
        None if not available (no such item).
        """
        index = number - 1
        if index >= 0 and index < len(self.items):
            print("You just bought a %s!\n" % self.items[index].getName())
            item = copy(self.items[index])
            return item
        else:
            print("I don't think we have that item...")
            return None

# ------------------------------------------------ #

def main():
    """test the store class"""
    items = loadItems("items.txt")    # from utils.py
    store = Store(items)              # create store from items
    print(store)                      # should print out store inventory
    fishes = 55                       # money to buy items with


    # follow the instructions and add your code below

    number = getInt("Select your item: ")

    if number == 0 or number > store.getNumItems():
        print("Fix that number, boi!")
    else:
        cost = store.getItemCost(number)
        if cost < fishes:
            store.buyItem(number)
        else:
            print("You don't have enough fishies")


if __name__ == "__main__":
    main()
