
class Pizza(object):
    def __init__(self, size):
        self.size = size   #either 'small' or 'large'
        self.toppings = [] #each topping should be a string
    def __str__(self):
        result = "Pizza (%s): " % (self.size)
        for i in range(len(self.toppings)):
            result += self.toppings[i] + " "
        return result
    def addTopping(self, item):
        self.toppings.append(item)
    def getPrice(self):
        if self.size == 'small':
            return 10 + len(self.toppings) * 0.5
        if self.size == 'large':
            return 12 + len(self.toppings) * 0.75

"""
Create a main program to test this class.  Make a small pizza with
pepperoni and onions.  Make a large pizza with pesto and spinach.
Print each pizza and its price.

Answer the following questions:
1. Define the term encapsulation
    An object containing info/methods
2. Define the term instance of a class

3. In what ways are methods and functions similar?
    They can both do an action
4. In what ways are methods and functions different?
    Methods know eveything about the object, unlike functions
    where variables are local. Also, they syntax in how they are called
    is a little different.
"""

def main():
    pizza1 = Pizza("large")
    pizza1.addTopping("pepperoni")
    pizza1.addTopping("onions")
    print("%s $%.2f" % (pizza1,pizza1.getPrice()))



main()
