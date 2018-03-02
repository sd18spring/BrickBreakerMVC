# -*- coding: utf-8 -*-
"""
This is a worked example of applying the Model-View-Controller (MVC)
design pattern to the creation of a simple arcade game (in this case
Brick Breaker).

We will create our game in stages so that you can see the process by
which the MVC pattern can be utilized to create clean, extensible,
and modular code.

@author: SoftDesProfs
"""

import pygame
from pygame.locals import *
import time

class PyGameWindowView(object):
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self, model, size):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height """
        self.model = model
        self.screen = pygame.display.set_mode(size)

    def draw(self):
        """ Draw the current game state to the screen """
        self.screen.fill(pygame.Color(0,0,0))
        for brick in self.model.bricks:
            pygame.draw.rect(self.screen,
                             pygame.Color(255, 255, 255),
                             pygame.Rect(brick.x,
                                         brick.y,
                                         brick.width,
                                         brick.height))
        pygame.display.update()

class BrickBreakerModel(object):
    """ Encodes a model of the game state """
    def __init__(self):
        self.bricks = []
        self.bricks.append(Brick(20, 100, 10, 10))

    def __str__(self):
        output_lines = []
        # convert each brick to a string for outputting
        for brick in self.bricks:
            output_lines.append(str(brick))
        # print one brick per line
        return "\n".join(output_lines)

class Brick(object):
    """ Encodes the state of a brick in the game """
    def __init__(self,height,width,x,y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def __str__(self):
        return "Brick height=%f, width=%f, x=%f, y=%f" % (self.height,
                                                          self.width,
                                                          self.x,
                                                          self.y)

if __name__ == '__main__':
    pygame.init()

    size = (640, 480)

    model = BrickBreakerModel()
    print(model)
    view = PyGameWindowView(model, size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        view.draw()
        time.sleep(.001)

    pygame.quit()
