"""
Class for holding restaurant information
"""
import json

class Restaurant:

    def __init__(self):
        """
        Constructor
        """
        self.data = {}

    def loadFromLine(self, line):
        """
        Initialize the values of this class based on text input
        Parameter line (str): a line of text in JSON format
        Return: none
        """
        self.data = json.loads(line)
        self.categories = self.data["categories"].split(",")

    def getName(self):
        """
        Accessor
        Return (str): the name of this restaurant
        """
        return self.data["name"]

    def getCity(self):
        """
        Accessor
        Return (str): the city where this restaurant is located
        """
        return self.data["city"]

    def getState(self):
        """
        Accessor
        Return (str): the two-letter state code where this restaurant is located
        """
        return self.data["state"]

    def getReviewCount(self):
        """
        Accessor
        Return (int): the number of reviews for this restaurant
        """
        return self.data["review_count"]

    def getStars(self):
        """
        Accessor
        Return (float): the number of stars for this restaurant
        """
        return self.data["stars"]

    def getCategories(self):
        """
        Accessor
        Return (list of str): the food categories for this restaurant, 
           exs: Korean, pizza, coffee, etc
        """
        return self.categories
