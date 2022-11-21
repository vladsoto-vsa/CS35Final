"""
Utilities for game
Date: 02-02-2021
"""
from item import *

def loadChoices(filename):
    """load choices data from file, return list of choice objs"""
    inf = open(filename,"r")
    lines = inf.readlines()
    inf.close()
    choices = []
    for line in lines:
        scenario,consequence,exp,cfoot,consq_alt,exp_alt,cfoot_alt,tag,ptag = line.strip().split(";")
        c = Item(scenario, consequence, int(exp), int(cfoot), consq_alt, int(exp_alt), int(cfoot_alt), tag, ptag)
        choices.append(c)
    return choices

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