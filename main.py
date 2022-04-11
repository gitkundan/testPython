from math import sqrt

class Point:
    """Defines point in space given x and y"""

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        """returns distance from point to origin"""
        return sqrt(self.x**2 + self.y**2)

    def reflect(self, axis):
        """shows the x inverse or y inverse co-ordinate of the point"""
        if axis == "x":
            self.y = -self.y
        elif axis == "y":
            self.x = -self.x
        else:
            print("The argument axis only accepts values x and y")

sample=Point(1.1,2.3)
sample.reflect("y")
print((sample.x,sample.y))
print(sample.distance_to_origin())