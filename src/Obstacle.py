import pygame


class Obstacle:
    """
    Used to create an obstacle of different parameters.

    :param x: The x location of the obstacle.
    :type x: int

    :param y: The y location of the obstacle.
    :type y: int

    :param length: the length of the obstacle.
    :type length: int

    :param width: The width of the obstacle.
    :type width: int

    :param color: The color of the obstacle.
    :type color: tuple(int,int,int)
    """
    def __init__(self, x=100, y=100, length=100, width=50, color=(0,0,255)):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.color = color
    

    def draw(self, screen):
        """
        Returns a render of an obstacle.

        :param screen: The screen to render the obstacle to.
        :type screen: pygame.display

	:return: A render of the obstacle.
	:rtype: pygame.draw.rect
        """
        return pygame.draw.rect(screen, self.color, (self.x, self.y, self.length, self.width), 0)

