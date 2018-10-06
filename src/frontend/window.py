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

    def __init__(self, screen):
        backgroundColor = colors.DARK_BLUE

        self.screen = screen
        pygame.display.set_caption("Test Window")
        self.screen.fill(backgroundColor)

    def init_window(self):
        """Initializes window"""
        pygame.display.init()
        pygame.display.flip()
                     
    def update_window(self, event, running):
        """Updates window, closes if user clicks close button"""
        pygame.display.update()
        
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
        for event in pygame.event.get():
            testWindow.update_window(event, running)


if __name__ == '__main__':
    main()
