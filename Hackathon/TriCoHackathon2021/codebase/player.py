
# Class of Player
class Player(object):
    # initialize, datatype:(str, int/float, int/float, bool)
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.exp = 0
        self.cfoot = 5
        self.choices = {} #a dictionary that stores the player's choices

    def getName(self):
        return self.name
    def getCountry(self):
        return self.country
    def getExp(self):
        return self.exp
    def getCarbonFoot(self):
        return self.cfoot
    
    def setExp(self, exp):
        self.exp+=exp
    def setCarbonFoot(self, cfoot):
        self.cfoot+=cfoot
    def addChoice(self, key, value):
        self.choices[key] = value
    


"""
# basic test codes below
# subject to changes
player0 = Player(exp, fp)
player0.showStats()
newChoice = input("What is your choice: ")  # only 'C1' works for now
print(choices[newChoice])
player0.modify(newChoice)
player0.showStats()
##### Kevin End #####
"""