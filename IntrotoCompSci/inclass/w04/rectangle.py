"""
Examples of functions
"""
def main():
    w = int(input("Enter width: "))
    l = int(input("Enter length: "))
    area = computeArea(l,w)
    print("area is", area)
    perim = computerPerimeter(l,w)
    print("perimeter is", perim)

def computeArea(length, width):
    return length * width

def computerPerimeter(length, width):
    return 2*(length + width)

main()
