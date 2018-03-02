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

if __name__ == '__main__':
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.001)

    pygame.quit()
