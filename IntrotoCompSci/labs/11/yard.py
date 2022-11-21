"""
Yard Class for Neko Atsume App

How yards work:
 - each yard has a certain number of slots for items
 - items get paired with cats when the cats come into the yard
 - a cat can't come into the yard if there are no available items in the yard
   (eg, if there are 3 items and 3 cats, no more cats allowed in yard)
 - if item is food, cat will eat it and both cat and item leave yard
 - when cats leave yard, they give gifts (fishes)

CS21
Spring 2020
"""

from utils import *

class Yard(object):
    """yard class...defines yard objects"""

    def __init__(self,nslots):
        """constructor for yard objects"""
        self.slots = {}          # key = item, value = cat
        self.limit = nslots      # limit on how many items yard can hold

    def __str__(self):
        """return string representation of yard obj"""
        s = "Here's your yard: \n"
        items = list(self.slots.keys())
        for i in range(self.limit):
            if len(items) > i:
                item = items[i]
                description = "  %d. %s" % (i+1,item.getName())
                if self.slots[item] != None:
                    # there's a cat paired with this item, so add cat name
                    description += ", %s" % self.slots[item].getName()
                description += "\n"
            else:
                description = "  %d. \n" % (i+1)   # no item in this slot
            s += description
        return s

    def updateFood(self):
        """check if food has been eaten, remove if yes, return fish"""
        totalfishes = 0
        items = list(self.slots.keys())
        for item in items:
            if item.isFood():
                if self.slots[item] != None:
                    # it's food, and there's a cat eating it
                    fishes = self.removeItem(item)
                    totalfishes += fishes
        return totalfishes

    def removeCat(self,cat):
        """removes a specific cat from the yard, give the gift of fishes"""
        fishes = 0
        for key in self.slots:
            c = self.slots[key]
            if c != None and c.getName() == cat.getName():
                # found the cat!
                self.slots[key] = None
                fishes = c.getFishes()
                print("\n<<<<< %s left the yard and gave you %d fishes!\n" % (c.getName(), fishes))
                return fishes
        return fishes

    def removeItem(self,i):
        """remove a specific item (and possibly a cat) from the yard"""
        # useful when cat eats the food item
        fishes = 0
        items = list(self.slots.keys())
        for item in items:
            if i.getName() == item.getName():
                # found the item!
                if self.slots[item] != None:
                    # there's a cat paired with this item, so remove cat too
                    fishes = self.removeCat(self.slots[item])
                self.slots.pop(item)
                return fishes
        return fishes

    def addSlot(self):
        """adds a slot to the yard (expands yard)"""
        self.limit += 1

    def numCats(self):
        """return number of cats currently in the yard"""
        ncats = 0
        for item in self.slots:
            c = self.slots[item]
            if c != None:
                ncats += 1
        return ncats

    def addItem(self,item):
        """add item to yard, if there's space"""
        if len(self.slots) < self.limit:
            self.slots[item] = None
        else:
            print("No space left in yard...")

    def addCat(self,cat):
        """add cat if there are available items"""
        if not self.empty():
            # there must be a toy to play with or food to eat
            items = self.slots.keys()
            for item in items:
                # and it must not already have a cat paired with it
                if self.slots[item] == None:
                   self.slots[item] = cat
                   print("\n>>>>> %s is in the yard!!!\n" % (cat.getName()))
                   return

    def empty(self):
        """return True if yard is empty (no items)"""
        return len(self.slots) == 0

    def full(self):
        """return True if no empty slots in yard"""
        return len(self.slots) == self.limit

    def itemAvailable(self):
        """return True if an item is available for a cat to play with/eat"""
        for item in self.slots:
            if self.slots[item] == None:
                return True
        return False

    def getCats(self):
        """return list of cats currently in the yard"""
        cats = []
        for item in self.slots:
            if self.slots[item] != None:
                cats.append(self.slots[item])
        return cats

# ------------------------------------------------ #

def main():
    """test the cat class"""
    cats = loadCats("cats.txt")       # from utils.py
    items = loadItems("items.txt")    # from utils.py
    yard = Yard(5)


    # follow the instructions and add your code below.
    print(yard)
    assert(yard.empty()==True)
    yard.addCat(cats[0])
    print(yard)
    yard.addItem(items[0])
    yard.addCat(cats[0])
    print(yard)
    yard.addItem(items[4])
    yard.addCat(cats[4])
    print(yard)
    yard.updateFood()
    #updateFood returns an updated amount of fishes
    listofCats = yard.getCats()
    yard.removeCat(cats[0])
    print(yard)
    #removeCat returns an amount of fishes



    # try to add cats[0] to the yard using addCat(cats[0])
    # and print the yard again...why isn't there a cat in the yard?
    # Hint: what does print(yard.itemAvailable()) print?


    # now add items[0] to the yard using addItem(items[0])
    # and then add cats[0] and print the yard. You should
    # see this:
    # >>>>> Tabitha is in the yard!!!
    #
    # Here's your yard:
    #   1. Rubber Ball, Tabitha
    #   2.
    #   3.
    #   4.
    #   5.



    # add items[4] to the yard (a food item) and cats[4]:
    # >>>>> Shadow is in the yard!!!
    #
    # Here's your yard:
    #   1. Rubber Ball, Tabitha
    #   2. Frisky Bitz, Shadow
    #   3.
    #   4.
    #   5.



    # if you call the updateFood() method, what happens?
    # and does updateFood() return anything?



    # call yard.getCats() to get a list of all cats in the yard,
    # and then print out all the cats in the list


    # if there are any cats still in the yard, remove them.
    # What does removeCat(..) return?


if __name__ == "__main__":
    main()
