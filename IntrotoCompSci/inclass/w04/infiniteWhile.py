"""
Example of infinite loop
"""

def main():
    x = 10
    while x > 0:
        print("x is", x)
        x = x + 1
        if x > 100:
            break



main()
