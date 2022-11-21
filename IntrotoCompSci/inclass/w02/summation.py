"""
Write psuedocode!


Ask user to what value they want to add, store as n
initialize start to 0
Loop n times
"""

def main():
    print("this program does a simple summation.")
    n = int(input("how many numbers to sum? "))
    total = 0
    for i in range(n+1):
        total += i
        print("Summation to", n, "is", total)

main()
