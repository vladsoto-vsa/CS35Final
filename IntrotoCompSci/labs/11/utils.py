"""
utilities for neko atsume cat game

CS21
Spring 2020
"""

from cat import *
from item import *

def loadItems(filename):
    """load item data from file, return list of item objs"""
    inf = open(filename,"r")
    lines = inf.readlines()
    inf.close()
    items = []
    for line in lines:
        name,cost,itype = line.strip().split(",")
        i = Item(name,int(cost),itype)
        items.append(i)
    return items

def loadCats(filename):
    """load cat data from file, return list of cat objs"""
    inf = open(filename,"r")
    lines = inf.readlines()
    inf.close()
    cats = []
    for line in lines:
        name,description,personality = line.strip().split(",")
        c = Cat(name,description,personality)
        cats.append(c)
    return cats

def menu(opts):
    """display menu, given a list, make sure we get valid menu input"""
    for i in range(len(opts)):
        print("%2d. %s" % (i+1,opts[i]))
    min = 1
    max = len(opts)
    while True:
        pick = getInt("Your choice? ")
        if pick >= min and pick <= max:
            return pick
        else:
            print("please enter a valid choice!!!")

def getInt(prompt):
    """get a positive integer"""
    n = input(prompt)
    if n.isdigit():
        return int(n)
    else:
        return getInt(prompt)
