"""
This program demonstrates how to read in a list of numbers from the
user (via a while loop with a flag).

It then passes the list of numbers into a function that computes and
returns their average.
"""

def main():
    # prompt the user to enter a series of numbers (-1 to stop)
    # append each number onto a list
    # call the average function to compute their average
    # print the result

    numbers = []
    level = 2
    while num != -1:
        numbers.append(num)
        num = int(input("enter a number, or -1 to quit"+str(level)+": "))
        level = level + 1
    print("the list contains", numbers)
    mean = average(numbers)
    print("Your list average is", mean)



def average(listofnums):
    """
    Input: A list of numbers.
    Returns: The average of the numbers.
    """
    total = 0
    for i in range(len(listofnums)):
        total += listofnums[i]
    avg = total / len(listofnums)
    return avg

main()
