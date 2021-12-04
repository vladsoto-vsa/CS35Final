"""
The main file that executes the game.
Date: 02-02-2021
"""
from utils import *
from player import *
import random

def main():
    player = intro()

    #load a scenario
    c_list = loadChoices("choices.txt")
    random.shuffle(c_list)
    
    for i in range(len(c_list)):
        print("-"*40)
        print("\n%s" %c_list[i].getScenario())
        opts = ["Yes", "No", "Quit"]
        pick = menu(opts)
        if pick == 1:
            player.addChoice(c_list[i].getTag(), True) #add choice to player data
            if c_list[i].getPTag() in player.choices: #check if prereq exists
                player.setExp(c_list[i].getExp()) #update player expenditure
                player.setCarbonFoot(c_list[i].getCarbonFoot()) #update player carbon footprint
                print("\n%s" %c_list[i].getConsq())
            else:
                player.setExp(c_list[i].getExpAlt()) #update player expenditure
                player.setCarbonFoot(c_list[i].getCarbonFootAlt()) #update player carbon footprint
                print("\n%s" %c_list[i].getConsqAlt())
            print("\nYour resulting Expenditure:", player.getExp())
            print("Your resulting Carbon Footprint Score:", player.getCarbonFoot(),"\n")
        elif pick == 2:
            print("K .")
        else:
            break
    
    endMsg(player.getExp(), player.getCarbonFoot())
    
    

#-----------------------------------------------------------------
"""
intro
prints the welcome message
"""
def intro():
    print("\nWelcome to Carbon President!")

    name = input("\nPlease enter your name: ")
    country_name = input("Please enter your country's name: ")

    print("\nGreetings, President %s. As a ruler, you will have to make choices that will either be good or bad for %s. To help you understand the power you hold, you will be tested on your basic understanding of sustainability." %(name, country_name))
    print("\nThe environment is important as it shapes the way we live. If you make the right choices, you will gain points for your carbon footprint, which is the measure of the amount of carbon dioxide (C02) from activities. Gaining carbon footprint points means you are helping the environment by lessening greenhouse gas emissions.")
    print("\nIf you make the wrong choices, you will gain expenditure points. Expenditure points are the money you will earn based on your choices. As a ruler, there is a lot that you can do with more money. If you do not have a sense of greed, you will lose expenditure points and help the environment too. Choices are hard to make, especially as a ruler, so you can quit anytime. Happy playing!\n")

    player = Player(name, country_name)
    return player

#-----------------------------------------------------------------   
def endMsg(exp, cfoot):
    print("\nYour final Expenditure:", exp)
    print("Your final Carbon Footprint Score:", cfoot,"\n")

    if exp < 3 and cfoot < 2:
        print("Nothing is impossible. Your brilliant leadership has restored more than the environment; it also restored people's relationship with the environment. Gone are the days of fighting against pollution. Now people have learned to respect and live in harmony with the environment")
    else:
        print("Your efforts to fight the climate crisis has paid off. Although there is still much to be done, humanity successfully avoided destruction...for now.")

main()