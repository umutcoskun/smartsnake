import math

class Point(object):
    def __init__(self, point, target=None):
        if isinstance(point, Point) and target is not None:
            # distance to the target point
            self.H = int(math.fabs(point.x - target.x) + math.fabs(point.y - target.y))

            self.x = point.x
            self.y = point.y

        else:
            # create static point
            self.x = point
            self.y = target

        self.target = target

    def detect_neighbors_except(self, blocks):
        neighbors = [
            self.add(0, -10),  # top
            self.add(10, 0),   # right
            self.add(0, 10),   # bottom
            self.add(-10, 0)   # left
        ]

        for point in neighbors:
            if not self.is_blocked(point, blocks):
                yield point

    def is_blocked(self, point, blocks):
        for block in blocks:
            if (block.x == point.x and block.y == point.y)\
                    or (point.x < 0 or point.y < 0 or point.x > 500 or point.y > 250):
                return True

        return False

    def add(self, x, y=0):
        return Point(Point(self.x + x, self.y + y), self.target)

    def __repr__(self):
        return "({} : {}) - {}".format(
            self.x,
            self.y,
            self.H
        )

    def __eq__(self, other):
        return self.H == other.H

    def __lt__(self, other):
        return self.H < other.H

    def __gt__(self, other):
        return self.H > other.H

    def __le__(self, other):
        return self.H <= other.H

    def __ge__(self, other):
        return self.H >= other.H