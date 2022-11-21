
class Point(object):
    """Class to represent two-dimensional points"""
    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y

    def toString(self):
        """Returns a string of all data in object"""
        return "x: %d y: %d" % (self.x, self.y)

    def setX(self, newx):
        """Setter method"""
        self.x = newx

    def setY(self, newy):
        """Setter method"""
        self.y = newy

    def getX(self):
        """Getter method"""
        return self.x

    def getY(self):
        """Getter method"""
        return self.y

def main():
    """Test out the Point class"""
    p1 = Point(1, 2)
    p2 = Point(5, 3)
    print(p1.toString())
    print(p2.toString())
    p1.setX(10)
    print(p1.getX())

main()
