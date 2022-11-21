"""
Name: Vladimir Soto-Avina
Date: 4/10/2020
Purpose: This program uses a real life dataset from Yelp, which provides
information about restaurants in several cities. The user is given three options
to either search for a restaurant, get restaurant statistics from a city, or
quit.
"""

from restaurant import *


def main():
    filename = "/home/alinen/public/cs21/restaurants.json"
    restaurantList = loadRestaurants(filename)
    print("="*8, "Welcome to Restaurant information", "="*8)
    opts = ["Restaurant Name", "City Query", "Quit"]
    done = False
    while done == False:
        selection = menu(opts)
        if selection == "1":
            userRestaurant = input("Enter a restaurant name: ")
            restaurantInfo = RestaurantSearch(userRestaurant, restaurantList)
            if restaurantInfo == -1:
                print("Not Found!")
            else:
                print(" "*10,"Name: ",restaurantInfo.getName())
                print(" "*10,"City: ", str(restaurantInfo.getCity())+", "+str(restaurantInfo.getState()))
                print(" "*10,"Reviews: ", restaurantInfo.getReviewCount())
                print(" "*10,"Stars: ", restaurantInfo.getStars())
                print(" "*10,"Categories: ", restaurantInfo.getCategories())

        elif selection == "2":
            userCity = input("Enter a city: ")
            userState = input("Enter initials of the state: ")
            cityStatInfo = cityStateStatistics(userCity, userState, restaurantList)

        else:
            done = True
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

#-------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------

def RestaurantSearch(resName, ls):
    """
    Inputs:  An item we are searching for and a SORTED list to search in
    Returns: Index of the found item in the list or -1 if not found
    Purpose: Does a binary search for the item in the SORTED list ls
    """
    resName = resName.lower()
    low_index = 0
    high_index = len(ls) - 1
    while low_index <= high_index:
        mid_index = int((low_index+high_index)/2)
        if resName == ls[mid_index].getName().lower():
            return ls[mid_index]
        elif resName < ls[mid_index].getName().lower():
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return -1
#-------------------------------------------------------------------------------
def cityStateStatistics(city, state, ls):
    """
    Purpose: This function uses the state and city entered by the user
    to find restaurant Statistics based on the list. If it doesn't find a
    matching city and/or state, then it will print no search results. If it
    does match, then it gives an overview of that city,state.

    Parameters:
        city -- city that user enters
        state -- state that user enters
        ls -- list
    Returns: None

    """
    count = 0
    avgStars = 0
    avgReviews = 0
    maxReviews = 0
    minReviews = ls[-1].getReviewCount()
    for i in range(len(ls)):
        if ls[i].getCity().lower() == city.lower() and ls[i].getState().lower() == state.lower():
            avgStars += ls[i].getStars()
            avgReviews += ls[i].getReviewCount()
            count += 1
            if ls[i].getReviewCount() > maxReviews:
                maxReviews = ls[i].getReviewCount()
            if ls[i].getReviewCount() < minReviews:
                minReviews = ls[i].getReviewCount()

    if count == 0:
        print("No search results for "+str(city)+","+str(state))
    else:
        avgStars = avgStars/count
        avgReviews = avgReviews/count
        print("Statistics for "+str(city)+","+str(state))
        print(" "*10, "Count: %36d" %(count))
        print(" "*10, "Average number of stars: %18.2f" %(avgStars))
        print(" "*10, "Average number of reviews: %16.2f" %(avgReviews))
        print(" "*10, "Max number of reviews: %20d" %(maxReviews))
        print(" "*10, "Min number of reviews: %20d" %(minReviews))






main()
