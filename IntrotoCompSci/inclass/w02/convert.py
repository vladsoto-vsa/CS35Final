"""
This program converts yards to meters.
1 yard is equivalent to 0.9144 meters.
"""

def main():
    # Get input about the number of yards to convert
    yards = float(input("Enter a yard amount to convert: "))
    # Calculate equivalent number of meters
    meters = yards * 0.9144
    # Print the results
    print("This is equilavent to", meters, "meters")

main()
