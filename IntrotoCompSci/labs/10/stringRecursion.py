"""
Name: Vladimir Soto-Avina
Date: 4/21/2020
Write a RECURSIVE solution to each of these string manipulation problems.
A main program has been provided to test them.
"""

#--------------------------------------------------------------------
def insert(string, add_char):
    """
    Inputs: A string and a character to insert
    Returns: A new string with the add_char inserted in between each
    character of the original string
    Examples:
      insert("swat", "*") returns "s*w*a*t"
      insert("I", "!") returns "I"
    """
    if len(string) == 1:
        return string
    else:
        return string[0] + add_char + insert(string[1:], add_char)



#--------------------------------------------------------------------
def remove(string, del_char):
    """
    Inputs: A string and a character to delete
    Returns: A new string with the del_char removed from the original
    string
    Examples:
      remove("banana", "a") returns "bnn"
      remove("zoo", "x") returns "zoo"
    """
    if len(string) == 1:
        return string
    elif string[0] == del_char:
        return remove(string[1:], del_char)
    else:
        return string[0] + remove(string[1:], del_char)


#--------------------------------------------------------------------
def repeat(string, n):
    """
    Inputs: A string and an interger
    Returns: A new string with the original string repeated n times
    Examples:
      repeat("tra", 3) returns "tratratra"
      repeat("hi", 1) returns "hi"
    """
    if n == 1:
        return string
    else:
        return string + repeat(string, n-1)



def main():
    print()
    print('Testing insert("swat", "*"):', insert("swat", "*"))
    print('Testing insert("I", "!"):', insert("I", "!"))
    print()
    print('Testing remove("banana", "a"):', remove("banana", "a"))
    print('Testing remove("zoo", "x"):', remove("zoo", "x"))
    print()
    print('Testing repeat("tra", 3):', repeat("tra", 3))
    print('Testing repeat("hi", 1):', repeat("hi", 1))
    print()

main()
