#!/usr/bin/env python3.6

import pygame

import sys
import os
sys.path.append(os.path.join(os.path.abspath(""),'frontend'))
sys.path.append(os.path.join(os.path.abspath(""), 'backend'))

from frontend import *

def main():
    pygame.init()
    clock = pygame.time.Clock()

    running = True

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
            if event.type == pygame.QUIT or keysPressed[pygame.K_q]:
                running = False
                pygame.display.quit()
                sys.exit()
            
        mainPlayer.update_loc_deltas(keysPressed)
        
        mainScreen.fill(backgroundImg)
        mainPlayer.update_loc(mainScreen)
        pygame.display.update()
        clock.tick(60) # in FPS

if __name__ == '__main__':
    main()
