#!/usr/bin/env python3.6

import pygame
import colors
import sys

class Window:
    """
    Base window class for starting the game and creating windows as necessary.

    Reference: http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/

    TODO: Resize behavior
    """

    def __init__(self, screen, backgroundImg):
        backgroundColor = backgroundImg

        self.screen = screen
        pygame.display.set_caption("Test Window")
        self.screen.fill(backgroundColor)

        pygame.display.init()
        pygame.display.flip()
