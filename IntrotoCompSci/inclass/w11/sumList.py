"""
Write a recursive function to sum up the items in a list.

sumList([5,3,1,4]) => 13

"""

def sumList(ls):

    if len(ls) == 0:
        return 0
    elif len(ls) == 1:
        return ls[0]
    else:
        return ls[0] + sumList(ls[1:])
