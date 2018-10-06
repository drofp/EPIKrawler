#!/usr/bin/env python3.6

import pygame

import sys
import os
sys.path.append(os.path.join(os.path.abspath(""),'frontend'))
sys.path.append(os.path.join(os.path.abspath(""), 'backend'))

import window

def main():
    pygame.init()

    running = True

    mainWindow = window.Window()
    mainWindow.init_window()

    # TODO: Event Loop
    while running:
        mainWindow.update_window(running)

    # TODO: Updating

    # TODO: Drawing

if __name__ == '__main__':
    main()
