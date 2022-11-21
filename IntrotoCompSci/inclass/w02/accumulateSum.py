"""
This program accumulates a sum of numbers entered by the user
"""

def main():
    n = int(input("How many numbers do you want to sum? "))
    total = 0
    for i in range(n):
        number = int(input("Enter a number: "))
        total = total + number
    print("The sum is:", total)

main()
