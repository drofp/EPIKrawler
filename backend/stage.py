"""
Author: Vinh Truong
"""

import items
import time
import pygame
from character_logic import characterLogic

tick = 0.02 # tick time in seconds

def run(character: characterLogic):
    # tracker = time.time() + tick
    while True:
        if character.move(1, 0):
            print(character.x, character.y)

if __name__ == "__main__":
    char = characterLogic(0, 10, 100, 10, 0.0, 0.0, 0.0)
    run(char)