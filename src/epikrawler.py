#!/usr/bin/env python3.6

import pygame
from pygame.locals import *

import sys
import os
sys.path.append(os.path.join(os.path.abspath(""), 'frontend'))
sys.path.append(os.path.join(os.path.abspath(""), 'backend'))

from frontend import *

def main():
    pygame.init()
    clock = pygame.time.Clock()

    running = True
    maxFPS = 60

    backgroundImg = colors.DARK_BLUE

    mainScreenW, mainScreenH = 500, 500
    mainScreen = pygame.display.set_mode((mainScreenW, mainScreenH))
    mainWindow = window.Window(mainScreen, backgroundImg)

    mainPlayerW, mainPlayerH = 100, 100
    mainPlayer = player_disp.PlayerDisplay(mainScreen, startX=mainScreenW/2 - mainPlayerW/2, 
                                            startY=mainScreenH/2 - mainPlayerH/2, rectChar=True)
    
    while running:
        # Main event loop
        keysPressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keysPressed[pygame.K_ESCAPE]:
                running = False
                pygame.display.quit()
                sys.exit()
            
        mainPlayer.update_loc_deltas(keysPressed)
        
        mainScreen.fill(backgroundImg)
        mainPlayer.update_loc(mainScreen)
        pygame.display.update()
        clock.tick(maxFPS)

        # For rough benchmarking runtime quickly
        # TODO: Show on window, like here: https://www.youtube.com/watch?v=HBbzYKMfx5Y
        print(clock.get_fps())

if __name__ == '__main__':
    main()
