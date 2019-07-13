import math


class Vector:
    """
    Vector class.

    Used to represent dots, velocities and accelerations. 
    For Dots, obstacles, and start/end points.

    :param x: the x location to travel to.
    :type x: float

    :param y: the y location to travel to.
    :type y: float
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def add(self, point):
        """
        Adds distance to the object.

        :param point: New distance.
        :type points: Vector
        """
        self.x += point.x
        self.y += point.y


    def distance_to(self, point):
        """ 
        Returns the distance to a given point.

        :param point: The point to calculate the distance to.
        :type point: Vector
        """
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        
