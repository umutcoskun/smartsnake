
from __future__ import print_function

from random import choice
import os

import pygame

from smartsnake import SmartSnake
from smartsnake.utils import Point
from smartsnake.exceptions import SnakeException

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Game(object):
    def __init__(self, display, flags, depth):
        pygame.init()
        pygame.display.set_caption('Smart Snake')
        pygame.display.set_icon(pygame.image.load('res/icon.png'))
        self.screen = pygame.display.set_mode(display, flags, depth)

        self.locate_apple()

    running = True
    clock = pygame.time.Clock()
    fps = 50

    snake = SmartSnake(Point(10, 10))
    apple = Point(50, 50)

    def loop(self):
        while self.running:
            self.events()
            self.update()
            self.render()
            self.clock.tick(self.fps)

    def update(self):
        try:
            collides = self.snake.step(self.apple)

            if collides:
                self.locate_apple()

        except SnakeException as e:
            print('Snake is dead.')

        except Exception as e:
            print('Exception: ', e)


    def locate_apple(self):
        width, height = self.screen.get_size()

        self.apple = Point(
            choice(xrange(10, width - 10, 10)),
            choice(xrange(10, height - 10, 10))
        )

    def render(self):
        self.screen.fill((255, 255, 255))

        self.draw(
            self.snake.body,
            (144, 198, 149)
        )

        self.draw(
            [self.apple],
            (246, 36, 89)
        )

        pygame.display.update()

    def draw(self, points, color):
        for point in points:
            if not isinstance(point, Point):
                break

            pygame.draw.rect(
                self.screen,
                color,
                pygame.Rect(
                    point.x,
                    point.y,
                    10, 10
                )
            )

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

if __name__ == "__main__":
    game = Game((500, 250), 0, 32)
    game.loop()