"""
Write a program using a while loop that counts down from a given
number and prints 'blastoff!' once the number hits 0. Below is an
example run.

Enter start of timer: 5
5
4
3
2
1
blastoff!
"""

def main():
    ignition = int(input("Enter start of timer: "))
    while ignition > 0:
        print(ignition)
        ignition = ignition - 1

    print("Blastoff!")

main()
