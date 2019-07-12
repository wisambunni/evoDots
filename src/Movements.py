from Vector import Vector


class Movements:
    """
    Movements class.
    Responsible for moving dots in the environment.

    :param start_point: Starting position of a dot.
    :type start_point: float.
    """
    def __init__(self, start_point):
        self.point = Vector(start_point.x, start_point.y)
        self.velocity = Vector(0,0)
        self.acceleration = Vector(0,0)
        self.x = self.point.x
        self.y = self.point.y

    
    def accelerate(self):
        """
        Accelerates a dot.
        """
        self.velocity.add(self.acceleration)
        self.point.add(self.velocity)


    def obstacle_hit(self, env):
        """
        Checks if a dot ran into an obstacle.

        :param env: The simulation environment.
        :type env: Environment.
        """
        for obstacle in env.obstacles:
            if (obstacle.x < self.point.x < obstacle.x+obstacle.length and
                obstacle.y < self.point.y < obstacle.y+obstacle.width):
                return True
        return False


    def wall_hit(self, env):
        """
        Checks if a dot ran into the wall.
        
        :param env: The simulation environment.
        :type env: Environment.
        """
        return not(0 < self.point.x < env.SCREEN_SIZE_X-2 and
                   0 < self.point.y < env.SCREEN_SIZE_Y-2)

    
    def goal_hit(self, env):
        """
        Checks if a dot ran into the goal.

        :param env: The simulation environment.
        :type env: Environment.
        """
        return self.point.distance_to(env.END_POINT) < 10
    



