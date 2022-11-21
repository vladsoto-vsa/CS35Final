"""
Convert a sequence of yards to meters and display the results as a table.
"""

def main():
    start = int(input("Where do you want the sequence to start? "))
    end = int(input("Where do you want your sequence to end? "))
    increment = int(input("What increment do you want to go by? "))
    print("Yds","Mtrs")
    print("---","----")
    for number in range(start,end+1,increment):
        print(number, number*0.9144)

main()
