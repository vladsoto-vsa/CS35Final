"""
A recursive implementation of binary search
"""

def binarySearch(ls,item):
    """
    Inputs: A sorted list ls and an item to search for in that list
    Returns: The index (int) of where the item was found in the list or
             -1 if the item was not found
    """
    return binarySearchRecur(ls,item, 0, len(ls)-1)


def binarySearchRecur(ls, item, low_index, high_index):
    """
    Inputs: A sorted list ls and an item to search for in that list, plus
    the boundaries of the indices where the item could be in the list.
    Returns: The index (int) of where the item was found in the lsit or
                -1 if the item was not found
    """
    if low_index > high_index:
        return -1
    mid_index = (low_index + high_index)//2
    if item == ls[mid_index]:
        return mid_index
    elif item < ls[mid_index]:
        return binarySearchRecur(ls, item, low_index, mid_index-1)
    else:
        return binarySearchRecur(ls, item, mid_index+1, high_index)
