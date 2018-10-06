#!/usr/bin/env python3.6

"""
Base window class for general window creation and resize behavior
"""

import pygame
import colors
import sys

class Window:
    """Base window class for starting the game and creating windows as necessary.
    
    Reference: http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/"""

    def __init__(self, screen, backgroundImg):
        backgroundColor = backgroundImg

        self.screen = screen
        pygame.display.set_caption("Test Window")
        self.screen.fill(backgroundColor)

    def init_window(self):
        """Initializes window"""
        pygame.display.init()
        pygame.display.flip()


def main():
    pygame.init()

    running = True

    testWindow = Window()
    testWindow.init_window()


if __name__ == '__main__':
    main()
