"""
neko atsume cat game

Name: Vladimir Soto-Avina
Date 5/1/2020
"""

from utils import *
from cat import *
from item import *
from yard import *
from store import *
from random import *

def main():
    cats = loadCats("cats.txt")
    items = loadItems("items.txt")
    store = Store(items)
    yard = Yard(5)
    album = []
    fishes = 200
    opts = ["see yard","shop","cat album", "quit"]
    done = False

    while not done:
        print("="*40)
        print("You've got %d fishes..." % (fishes))
        pick = menu(opts)
        if pick == 1:
            display(yard)
        elif pick == 2:
            if yard.full():
                print("Your yard is already full...")
            else:
                fishes = shop(store,yard,fishes,items)
        elif pick == 3:
            show(album)
        elif pick == 4:
            done = True
        fishes = update(yard,cats,album,fishes)
    print("\nMeow....\n")

def display(yard):
    """
    Purpose: prints the yard
    Parameters: yard class
    Returns:
    """
    print(yard)

def shop(store,yard,fishes,items):
    """
    Purpose: Uses the store class to allow user to purchase items,
            which are added to the yard, using fishes.
    Parameters:
        store -- store class
        yard -- yard class
        fishes -- amount of fishes
        items -- item class
    Returns:
        amount of fishes

    """
    print(store)
    number = getInt("Select your item: ")
    if number == 0:
        return fishes
    elif number > store.getNumItems():
        print("Fix that number, boi!")
    else:
        cost = store.getItemCost(number)
        if cost < fishes:
            item = store.buyItem(number)
            fishes = fishes - cost
            yard.addItem(item)
        else:
            print("You don't have enough fishies")
    return fishes


def update(yard,cats,album,fishes):
    """
    Purpose: This function updates the cats in the yard, the amount of fishes,
            and the cats in the Album
    Parameters:
        yard -- yard class
        cats -- cats class
        album -- list of cats and their details
        fishes -- amount of fishes
    Returns:
        fishes
    """
    if yard.empty() == True:
        return fishes

    else:
        newfishes = yard.updateFood()
        fishes = fishes + newfishes
        if yard.numCats() > 0:
            random = randrange(0,2)
            if random == 1:
                catsyard = yard.getCats()
                newfishes = yard.removeCat(catsyard[0])
                fishes = fishes + newfishes

        if yard.itemAvailable() == True:
            random2 = randrange(0,2)
            if random2 == 1:
                randcat = randrange(0,len(cats))
                yard.addCat(cats[randcat])
                if cats[randcat] not in album:
                    album.append(cats[randcat])
                cats[randcat].visited()
        return fishes


def show(album):
    """
    Purpose: This prints a list of all the cats that been in the yard,
            along with amount of Visits
    Parameters:
        album -- list of cats
    Returns:
    """
    print("."*10, "Cat Album", "."*10)
    number = 1
    for cats in album:
        print(str(number)+".", "Name:", cats.getName(), "("+cats.getDescription()
        +")"+ ", Visits:", cats.getVisits())
        number += 1






main()
