"""
This program checks if the items in a list have positive integers
"""

def main():
    tests = ["123","1 2 3","zebra","99","99!","-99"]
    for i in range(len(tests)):
        print("%d: %6s  %5s" % (i,tests[i],alldigits(tests[i])))

# add your function here
def alldigits(string):
    """
    Purpose: it checks whether or not a string has an integer and only ints
    Parameters: string -- serves as the list based on tests
    Return: false and true. if it's false, means the item on the list has non
    positive-integers
    """
    numbers = ["0","1","2","3","4","5","6","7","8","9"]


    for i in range(len(string)):
        if string[i] not in numbers:
            return False


    return True






main()
