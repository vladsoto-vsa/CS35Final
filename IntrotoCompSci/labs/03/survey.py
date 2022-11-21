"""
With setup information, the program compares the user's input to the info
"""

def main():
    topics = ["color", "food", "season", "holiday"]
    preferences = ["blue", "tacos", "fall", "christmas"]
    matches = 0
    for i in range(len(topics)):
        answer = input("What is your favorite " + topics[i] + "? ")

        if answer == preferences[i]:
            matches = matches + 1
            print("That is my favorite " + topics[i] + " too")

        else:
            print("nah")

    if matches == 4:
            print("We are soul mates, bruh")
    elif matches < 4 and matches > 0:
            print("We got some things in common")
    else:
            print("Nah, bruh")

main()
