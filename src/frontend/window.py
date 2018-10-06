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
    def __init__(self):
        backgroundColor = colors.DARK_BLUE
        (self.width, self.height) = (500, 500)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Test Window")
        self.screen.fill(backgroundColor)


    def init_window(self):
        """Initializes window"""
        pygame.display.init()
        pygame.display.flip()
                     
    def update_window(self, running):
        """Updates window"""
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                sys.exit()


def main():
    pygame.init()

    running = True

    testWindow = Window()
    testWindow.init_window()

    while running:
        testWindow.update_window(running)


if __name__ == '__main__':
    main()
