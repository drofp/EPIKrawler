#!/usr/bin/env python3.6

import pygame
from pygame.locals import *

import collections
import os
import sys

import configparser

sys.path.append(os.path.join(os.path.abspath(""), 'frontend'))
sys.path.append(os.path.join(os.path.abspath(""), 'backend'))

from frontend import *

DISPLAY_CONFIG_PATH = 'frontend/display_opt.ini'


def parse_display_config(display_config_path):
    config = configparser.ConfigParser()
    config.read(display_config_path)
    return config


def get_startup_params():
    """Return a tuple of startup params"""
    config = parse_display_config(DISPLAY_CONFIG_PATH)
    startup_params = collections.namedtuple('StartupParam', 'MaxFps')
    startup_params.MaxFps = int(config['LIMITS']['MaxFps'])
    return startup_params


def main():
    startup_params = get_startup_params()
    pygame.init()
    clock = pygame.time.Clock()

    running = True
    maxFPS = startup_params.MaxFps

    backgroundImg = colors.DARK_BLUE

    displayInfo = pygame.display.Info()
    mainScreenW, mainScreenH = displayInfo.current_w, displayInfo.current_h
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
