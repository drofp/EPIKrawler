#!/usr/bin/env python3.6

import pygame

import sys
import os
sys.path.append(os.path.join(os.path.abspath(""),'frontend'))
sys.path.append(os.path.join(os.path.abspath(""), 'backend'))

import window

def main():
    pygame.init()

    testWindow = window.Window()
    testWindow.init_window()

if __name__ == '__main__':
    main()
