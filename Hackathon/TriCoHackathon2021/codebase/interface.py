from tkinter import *

# home page
# window
homePage = Tk()
homePage.geometry('400x150')
homePage.title('Welcome to the [GAME]')

# name label and name entry box
nameLabel = Label(homePage, text="Please enter your name:").grid(row=0, column=0)
name = StringVar()
nameEntry = Entry(homePage, textvariable=name).grid(row=0, column=1)

# country label and country entry box
countryLabel = Label(homePage, text="Please enter your country's name:").grid(row=1, column=0)
country = StringVar()
countryEntry = Entry(homePage, textvariable=country, show='*').grid(row=1, column=1)


# start game button
def startGame():
    pass


startButton = Button(homePage, text="Start!", command=startGame).grid(row=4, column=0)

homePage.mainloop()
