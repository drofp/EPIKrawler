#!/usr/bin/env python3.6

"""Base window class for general window creation and resize behavior"""

import pygame

class Window(object):
    """Reference: http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/"""
    def __init__(self):
        
        self.running = True
        (self.width, self.height) = (500, 500)
        self.screen = pygame.display.set_mode((self.width, self.height))

    def init_window(self):
        
        pygame.display.init()
        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.display.quit()
                    
def main():
    pygame.init()

    testWindow = Window()
    testWindow.init_window()


if __name__ == '__main__':
    main()
