"""
Using a loop to exponentially grow number of party guests
and string accumulation to show how many ppl
"""

def main():
    friends = int(input("Enter your number of close friends: "))
    print("You invite " + str(friends) + " friends")
    people = 0

    for i in range(2,8):
        print("Your "+ "friends " *(i-1) + " invite " + str(friends ** i) + " more people!")
        people = people + friends ** i

    print("You expect " + str(people) + " people at your party!")
main()
