def isSorted(ls):
    """
    Input: a list of items
    Returns: True when the list is in ascending order
    or False when it is not
    """
    for i in range(len(ls)-1):
        if ls[i] > ls[i+1]:
            return False
    return True
