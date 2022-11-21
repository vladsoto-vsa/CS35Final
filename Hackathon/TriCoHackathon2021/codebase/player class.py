##### Kevin Start #####
# Scenarios and starting conditions for exp and fp (adjust based on character/difficulty)
stats = [(0, 0), (1, 1)]  # dummy assignment in the format of (exp,fp)

# dummy base stats
# expenditure
exp = stats[0][0]  # dummy assignment
# carbon footprint
fp = stats[0][1]  # dummy assignment

# dictionary of Choices in the format of 'name': (changeExp, changeFp, good_or_bad)
choices = {
    'C1': (-1, -1, True)
}

# Class of Player
class Player:
    # initialize, datatype:(str, int/float, int/float, bool)
    def __init__(self, exp, fp):
        self.exp = exp
        self.fp = fp

    def showStats(self):
        print("The player currently has expenditure %s and carbon footprint %s" % (self.exp, self.fp))

    #def modifyExp(self, expChange):
    #    self.exp += expChange
    #    print("the new exp is %s" % self.exp)

    #def modifyFp(self, fpChange):
    #    self.fp += fpChange
    #    print("the new fp is %s" % self.fp)

    def modify(self, newChoice):
        self.exp += choices[newChoice][0]
        self.fp += choices[newChoice][1]
        print("the new exp is %s, the new fp is %s" % (self.exp, self.fp))

# basic test codes below
# subject to changes
player0 = Player(exp, fp)
player0.showStats()
newChoice = input("What is your choice: ")  # only 'C1' works for now
print(choices[newChoice])
player0.modify(newChoice)
player0.showStats()
##### Kevin End #####