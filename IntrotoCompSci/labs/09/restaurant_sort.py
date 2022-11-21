"""
Name: Vladimir Soto-Avina
Date: 4/15/2020
Purpose: This program uses a real life dataset, to which the user can input keywords,
        or certain criteria, to get a list of restaurants that matches the criteria. 

"""

from restaurant import *
def main():
        filename = "/home/alinen/public/cs21/restaurants.json"
        restaurantList = loadRestaurants(filename)
        print("="*8, "Welcome to Restaurant information", "="*8)
        opts = ["Search Names", "Plan a night out", "Quit"]
        done = False
        while done == False:
            print(" ")
            selection = menu(opts)
            if selection == "1":
                userSearch = input("Enter a keyword: ")
                searchResults = searchKeyword(userSearch, restaurantList)
                if len(searchResults) == 0:
                    print("None found")
                else:
                    orderedResults = sortSearch(searchResults)
                    printResults(orderedResults)



            elif selection == "2":
                userCity = input("Enter a city: ")
                userState = input("Enter initials of the state: ")
                keyword = input("Enter a name keyword: ")
                searchResults = planNight(userCity, userState, keyword, restaurantList)
                if len(searchResults) == 0:
                    print("None found")
                else:
                    orderedResults = sortSearch(searchResults)
                    printResults(orderedResults)

            else:
                done = True



#==============================================================================
def loadRestaurants(filename):
    """
    Purpose: Accesses information from a dataset
    Parameter:
        filename -- file that is accessed
    Returns: a list of restaurants taken from the dataset
    """
    ifile = open(filename, "r")
    restaurantList = []
    for line in ifile:
        restaurant = Restaurant()
        restaurant.loadFromLine(line)
        restaurantList.append(restaurant)
    return restaurantList
#==============================================================================
def menu(options):
    """
    Purpose: Using the alldigits function, this prevents a user from choosing
    an option outside of the range or a string
    Parameters:
        options -- uses the opts list
    Returns:
        selection -- returns the option the user enters
    """
    for i in range(len(options)):
        print(str(i+1)+".", options[i])
    done = False
    while not done:
        selection = input("your choice --> ")
        if alldigits(selection) == False:
            print("please enter a positive integer")

        elif int(selection) > len(options) or int(selection) < 1:
            print("please enter a valid choice!!!")

        else:
            done = True
    return selection
#==============================================================================
def alldigits(string):
    """
    This function returns true if all of the characters in the string
    are digits. If they're not, then it returns false
    """
    numbers = ["0","1","2","3","4","5","6","7","8","9"]


    for i in range(len(string)):
        if string[i] not in numbers:
            return False

    return True
#==============================================================================

def searchKeyword(search,ls):
    """
    Purpose: This function searches through a list to see if a user's search
            for a keyword appears in the list
    Parameters:
        search -- keyword user Inputs
        ls - list that is searched
    Returns:

    """
    search = search.lower()
    results = []

    for i in range(len(ls)):
        if search in ls[i].getName().lower():
            results.append(ls[i])

    return results


def sortSearch(searchResults):
    """
    Purpose: This function uses bubble sort to organize a list by reviews
    Parameters:
        searchResults -- list that is used
    Returns:
        updated list
    """
    count = 0

    for n in range(len(searchResults)):
        for j in range(1,len(searchResults)-n):
            if searchResults[j-1].getReviewCount() < searchResults[j].getReviewCount():
                r = searchResults[j-1]
                searchResults[j-1] = searchResults[j]
                searchResults[j] = r
    return searchResults


#==============================================================================


def planNight(city, state, keyword, ls):
    """
    Purpose: This function searches through a list using three criteria the
                user inputs: city, state, and keyword
    Parameters:
        city -- city user Inputs
        state -- state user Inputs
        keyword -- keyword user Inputs
        ls -- list that is used to search through
    Returns: returns a new list of items that matched the criteria
    """
    city = city.lower()
    state = state.lower()
    keyword = keyword.lower()
    results = []

    for i in range(len(ls)):
        if keyword in ls[i].getName().lower():
            if city == ls[i].getCity().lower() and state == ls[i].getState().lower():
                results.append(ls[i])
    return results

#==============================================================================
def printResults(searchResults):
    """
    Purpose: This function prints out information of restaurants using methods
    Parameters:
        searchResults -- list that is used to print info about items
    Returns: none

    """
    end = 25
    print(" "*18, "Restaurant", " "*18, "Location", " "*10, "Reviews", " "*10, "Stars")
    print(" "*18, "==========", " "*18, "========", " "*10, "=======", " "*10, "=====")
    if len(searchResults) < 25:
        end = len(searchResults)

    for i in range(end):
        restaurant = searchResults[i]
        Name = restaurant.getName()

        city = restaurant.getCity()
        state = restaurant.getState()
        reviews = restaurant.getReviewCount()
        stars = restaurant.getStars()
        print("%29s %24s %1s %18s %16s" %(Name, city, state, reviews, stars))
    print(" ")
    print("Showing", end, "out of", len(searchResults), "restaurants")






main()
