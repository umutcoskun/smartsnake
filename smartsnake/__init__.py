from __future__ import print_function

import math

from utils import Point
from exceptions import *

class SmartSnake(object):
    def __init__(self, position):
        self.body = [position]

    body = [] # FIFO

    @property
    def head(self):
        return self.body[-1]

    @head.setter
    def head(self, point):
        self.body.append(point)

    def step(self, target):
        if not isinstance(target, Point):
            TypeError('target must be Point')

        # add head at the new position
        self.head = self.find_path_to(target)

        # Collision control with the target
        if len(self.body) > 1 and not self.is_colliding_with(target):
            self.body.pop(0)

        return self.is_colliding_with(target)

    def find_path_to(self, target):
        blocks = [Point(point, target) for point in self.body]
        head = Point(self.head, target)

        neighbors = head.detect_neighbors_except(blocks)
        selected = min(neighbors)

        return selected

    def is_colliding_with(self, points):
        if not isinstance(points, list): points = [points]

        for target in points:
            if any([
                    # Simple collision control
                    (target.x + 10 >= point.x and target.x <= point.x + 10) and
                    (target.y + 10 >= point.y and target.y <= point.y + 10)
                    for point in self.body
                ]): return True

        return False

    def get_distance_from(self, other):
        return Point(math.fabs(self.head.x - other.x), math.fabs(self.head.y - other.y))