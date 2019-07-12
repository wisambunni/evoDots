import pygame
import sys
import random 

from Vector import Vector
from Obstacle import Obstacle
# from Population import Population

# SCREEN_SIZE_X = 1920
# SCREEN_SIZE_Y = 1080

class Environment:
    """
    Used to create the environment for the simulation

    :param screen_width: The width of the screen.
    :type screen_width: int

    :param screen_height: The height of the screen.
    :type screen_height: int
    """
    def __init__(self, screen_width, screen_height):
        # pygame.init()
        self.SCREEN_SIZE_X = screen_width
        self.SCREEN_SIZE_Y = screen_height
        self.screen = pygame.display.set_mode((self.SCREEN_SIZE_X,
                                               self.SCREEN_SIZE_Y))

        self.line_points = []
        self.obstacles = []
        self.screen.fill((255,255,255))
        self.create_start_end_points()
        self.create_obstacles(10)


    def create_start_end_points(self):
        """
        Defines start and end points.
        """
        # Start x,y values
        x = random.randint(100, self.SCREEN_SIZE_X-100)
        y = int(5 * self.SCREEN_SIZE_Y / 6)
        self.START_POINT = Vector(x,y)

        # End x,y values
        x = random.randint(100, self.SCREEN_SIZE_X-100)
        y = int(self.SCREEN_SIZE_Y / 6)
        self.END_POINT = Vector(x,y)


    def create_obstacles(self, size):
        """
        Creates obstacles of random shape, size, and location.

        :param size: The number of obstacles to create.
        :type size: int.
        """
        # minimum distance an obstacle should spawn from either start or end points.
        min_from_start = int(self.START_POINT.y - (self.START_POINT.y*.2))
        min_from_end = int(self.END_POINT.y + (self.END_POINT.y*.2))

        # minimum and maximum lengths the obstacles can be
        min_len = int(self.SCREEN_SIZE_X * 0.05)
        max_len = int(self.SCREEN_SIZE_X * 0.3)

        # min and max width the obstacle can be
        min_width = 10
        max_width = 50

        x_boundary = int(self.SCREEN_SIZE_X * 0.05)

        for i in range(size):
            length = random.randint(min_len, max_len)
            width = random.randint(min_width, max_width)
            x = random.randint(x_boundary, self.SCREEN_SIZE_X-x_boundary-length)
            y = random.randint(min_from_end, min_from_start)

            self.obstacles.append(Obstacle(x=x, y=y, length=length, width=width))


    def redraw(self, population):
        """
        Draws a new frame.

        :param population: The population sample for the simulation.
        :type population: Population
        """
        self.screen.fill((255,255,255))
        pygame.font.init()

        font = pygame.font.SysFont('Arial', 30)

        text_area = font.render('GENERATION: ' + str(population.generation), False, (0,0,0))
        self.screen.blit(text_area, (int(self.SCREEN_SIZE_X/2), self.START_POINT.y + 100))

        text_area = font.render('MIN-STEPS    : ' + str(population.min_step), False, (0,0,0))
        self.screen.blit(text_area, (int(self.SCREEN_SIZE_X/2), self.START_POINT.y + 130))

        # Start point
        pygame.draw.circle(self.screen, (0,255,0), (self.START_POINT.x, self.START_POINT.y), 10)
        # End point
        pygame.draw.circle(self.screen, (255,0,0), (self.END_POINT.x, self.END_POINT.y), 10)

        for dot in population.samples:
            if dot.most_fit:
                self.line_points.append((dot.movement.point.x, dot.movement.point.y))
                pygame.draw.lines(self.screen, (0,255,0), False, self.line_points, 3)
                # pygame.draw.rect(self.screen, (0,255,0), (dot.movement.point.x, dot.movement.point.y, 5, 5), 0)
            else:
                # pygame.draw.rect(self.screen, dot.color, (dot.movement.point.x, dot.movement.point.y, 5, 5), 0)
                pygame.draw.circle(self.screen, dot.color, (int(dot.movement.point.x), int(dot.movement.point.y)), 3)
        
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        pygame.display.update()


    def clear(self):
        """
        Clears the line of the most fit dot.
        """
        self.line_points = [(self.START_POINT.x, self.START_POINT.y)]
    

    def exited(self):
        """
        Graceful way to exit pygame.
        """
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()