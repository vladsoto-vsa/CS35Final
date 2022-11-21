import random



def main():

    userwins = 0
    botwins = 0
    turns = 0
    options = ["rock","paper","scissors"]




    userchoice = getPick()
    botchoice = random.choice(options)

    roundwin = winner(userchoice, botchoice)
    turns = turns + 1
    print("I chose", botchoice)
    if roundwin == "comp":
        print("I win")
        botwins = botwins + 1
    elif roundwin == "user":
        print("You win")
        userwins = userwins + 1
    elif roundwin == "tie":
        print("Tie")


def getPick():
    choice = input("r,p,s? ")
    choice = choice.lower()
    if choice == "r":
        return "rock"
    elif choice == "p":
        return "paper"
    elif choice == "s":
        return "scissors"
    else:
        print("please enter r, p, or s!!!")

def winner(user, comp):
    "rock" > "scissors"
    "paper" > "rock"
    "scissors" > "paper"

    if user > comp:
        return "user"
    elif user < comp:
        return "comp"
    else:
        return "tie"


main()
