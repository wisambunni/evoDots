import pygame
import random
import math

from Dot import Dot
from Environment import Environment


class Population:
    """
    Population class.
    Consists of Dots used for the simulation.

    :param size: Quantity of dots.
    :type size: int.

    :param env: Environment that population is working in.
    :type env: Environment.
    """
    def __init__(self, size, env):
        self.POPULATION_SIZE = size
        self.ENV = env
        self.POSSIBLE_STEPS = env.SCREEN_SIZE_X * env.SCREEN_SIZE_Y

        self.samples = []
        self.fitness_sum = 0
        self.generation = 1
        self.best_dot = 0
        self.min_step = self.POSSIBLE_STEPS

        Dot.dead = 0

        for i in range(self.POPULATION_SIZE):
            self.samples.append(Dot(self.ENV.START_POINT))
    

    def move_dots(self):
        """
        Moves a dot in the simulation environment
        """
        for dot in self.samples:
            dot.make_decision(self.ENV, self.POSSIBLE_STEPS)
    

    def extinct(self):
        """
        Determines whether all the dots in the population are dead
        """
        return Dot.dead == self.POPULATION_SIZE

    
    def perform_natural_selection(self):
        """
        Assigns the best parent for the next generation based on the parent
        with the best fitness score.
        """
        next_generation = [Dot(self.ENV.START_POINT)] * len(self.samples)

        self.set_best_dot()
        self.calculate_fitness_sum()

        next_generation[0] = self.samples[self.best_dot].make_baby(self.ENV.START_POINT)
        next_generation[0].most_fit = True

        for dot in range(1, len(next_generation)):
            #select parent
            parent = self.select_parent()

            #then get offspring
            next_generation[dot] = parent.make_baby(self.ENV.START_POINT)
        
        self.samples = next_generation
        self.generation += 1
        Dot.dead = 0
        self.fitness_sum = 0


    def calculate_fitness(self):
        """
        Calculates the fitnes score of each dot.
        """
        for dot in self.samples:
            dot.calculate_fitness(self.ENV) 


    def calculate_fitness_sum(self):
        """
        Calculates the fitness sum for all the dots in the population.
        This will be used to determine the best parent.
        """
        self.fitness_sum = 0
        for dot in self.samples:
            self.fitness_sum += dot.fitness
    

    def select_parent(self):
        """
        Selects a parent for the next generation based on the best fitness score.
        """
        rand = random.uniform(0, self.fitness_sum)

        running_sum = 0
        for dot in self.samples:
            running_sum += dot.fitness
            if running_sum > rand:
                return dot


    def mutate_babies(self):
        """
        Mutates all of the next generation of dots.
        Note: The most fit dot of the previous generation is immortal and moved
        into the next generation without mutating, hence the range(1,...).
        """
        for dot in range(1, len(self.samples)):
            self.samples[dot].genetics.mutate()


    def set_best_dot(self):
        """
        Select the best performing dot out of a generation. 
        The most 'fit' dot is defined as one that has the highest fitness score
        and the least amount of steps taken to get to the goal (or as close to).
        """
        max_fitness = 0.0 
        max_idx = 0
        for d in range(len(self.samples)):
            if self.samples[d].fitness > max_fitness:
                max_fitness = self.samples[d].fitness
                max_idx = d
        
        self.best_dot = max_idx
    
        if self.samples[self.best_dot].goal_found:
            min_step = self.samples[self.best_dot].genetics.step
            self.min_step = min_step


