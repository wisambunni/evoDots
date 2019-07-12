import pygame
from Environment import Environment
from Population import Population
from Genetics import Genetics
from time import sleep

ENV = Environment(1920,1080)
POPULATION = Population(1000, ENV)

while True:
    ENV.exited()
    if not POPULATION.extinct():
        ENV.exited()
        POPULATION.move_dots()
        ENV.redraw(POPULATION)
    else:
        ENV.clear()
        POPULATION.calculate_fitness()
        POPULATION.perform_natural_selection()
        POPULATION.mutate_babies()

