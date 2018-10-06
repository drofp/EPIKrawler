#!/usr/bin/env python3.6

import pygame

import sys
import os
sys.path.append(os.path.join(os.path.abspath(""),'frontend'))
sys.path.append(os.path.join(os.path.abspath(""), 'backend'))

from frontend import *

def main():
    pygame.init()
    pygame.time.Clock()

    running = True

    mainScreenW, mainScreenH = 500, 500
    mainScreen = pygame.display.set_mode((mainScreenW, mainScreenH))
    mainWindow = window.Window(mainScreen)
    mainWindow.init_window()

    mainPlayerW, mainPlayerH = 100, 100
    mainPlayer = character.CharacterDisplay(mainScreen, startX=mainScreenW/2 - mainPlayerW/2, 
                                            startY=mainScreenH/2 - mainPlayerH/2, rectChar=True)
    while running:
        # Main event loop
        for event in pygame.event.get():
            mainWindow.update_window(event, running)

if __name__ == '__main__':
    main()
