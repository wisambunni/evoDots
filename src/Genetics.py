import pygame
import random
import math

from Vector import Vector


class Genetics:
    """
    The brain of the dot.
    Used to determine the path to take in the envinroment.

    :param size: The size of the population.
    :type size: int.
    """
    def __init__(self, size):
        self.size = size
        self.directions = []
        self.step = 0
    
        self.randomize()
    

    def randomize(self):
        """
        Randomizes the directions of a dot.
        """
        for i in range(self.size):
            # Choose a random angle
            x = random.random() * (2*math.pi)

            self.directions.append(Vector(math.cos(x), math.sin(x)))
    

    def clone(self):
        """
        Clones the current directions of a dot.
        """
        clone = Genetics(len(self.directions))
        for i in range(len(self.directions)):
            clone.directions[i] = self.directions[i]
        
        return clone
    

    def mutate(self):
        """
        Mutates the directions of a dot.
        """
        # The chance a specific direction will be overridden by a random one.
        mutation_rate = 0.01
        for d in range(len(self.directions)):
            rand = random.random()
            if rand < mutation_rate:
            # Set this direction as a random direction
                x = random.random() * (2*math.pi)
                self.directions[d] = Vector(math.cos(x), math.sin(x))


    def reset_steps(self):
        """
        Resets the number of steps a dot has taken.
        """
        self.step = 0

