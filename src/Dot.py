import pygame
import random
import math
import numpy as np

from Movements import Movements
from Vector import Vector
from Environment import Environment
from Genetics import Genetics

class Dot:
    """
    The smallest unit in the population.
    Used to represent the "beings" in the simulation.

    :param start_point: The starting position of the dot.
    :type start_point: Vector.
    """
    dead = 0
    def __init__(self, start_point):
        self.color = (100,100,100)
        self.fitness = 0
        self.alive = True
        self.goal_found = False
        self.obstacle_hit = False
        self.most_fit = False
        self.movement = Movements(start_point)
        self.genetics = Genetics(1000)


    def make_decision(self, env, steps_in_path):
        """
        Make a decision based on the environmental conditions.

        :param env: The simulation environment.
        :type env: Environment.

        :param steps_in_path: The number of steps possible in the environment.
        :type steps_in_path: int.
        """

        if self.is_alive(env):
            if len(self.genetics.directions) > self.genetics.step:
                self.movement.acceleration = self.genetics.directions[self.genetics.step]
                self.genetics.step += 1
            else:
                self.alive = False
            
            if self.genetics.step > steps_in_path:
                self.alive = False
            self.movement.accelerate()
    

    def calculate_fitness(self, env):
        """
        Calculate the fitness of a dot. That is, how close did the dot get
        to the goal.
        
        :param end_point: The end point.
        :type end_point: Vector.
        """
        # Reward dots that find the goal.
        if self.goal_found:
            self.fitness = (1.0/16.0) + (10000.0/(self.genetics.step**2))

        # Severely punish dots that run into obstacles.
        elif self.obstacle_hit:
            distance_to_goal = self.movement.point.distance_to(env.END_POINT)
            self.fitness = 1.0/(100000+distance_to_goal**2)

        # Default fitness for the rest.
        else:
            distance_to_goal = self.movement.point.distance_to(env.END_POINT)
            self.fitness = 1.0/(distance_to_goal**2)

        return self.fitness


    def is_alive(self, env): 
        """
        Determines whether a dot has ran into the edges of the screen
        or into the goal.

        :param env: The simulation environment.
        :type env: Environment.
        """
        # Check if a dot hits the edge of the env
        if self.alive and self.movement.wall_hit(env):
            Dot.dead += 1
            self.alive = False

        if self.alive and self.movement.obstacle_hit(env):
            Dot.dead += 1
            self.alive = False
            self.obstacle_hit = True

        if self.alive and self.movement.goal_hit(env):
            Dot.dead += 1
            self.alive = False
            self.goal_found = True
        

        return self.alive

    
    def make_baby(self, start_point):
        """
        Creates a clone based on the current dot.
        
        :param start_point: The starting point of the dot.
        :type start_point: Vector.
        """
        baby = Dot(start_point)
        baby.genetics = self.genetics.clone()

        return baby
