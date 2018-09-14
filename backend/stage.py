"""
Author: Vinh Truong
"""

import Items
import time
import pygame
from Character import Character

tick = 0.02 # tick time in seconds

def run(character: Character):
    # tracker = time.time() + tick
    while True:
        if character.move():
            print(character.x, character.y)

if __name__ == "__main__":
    char = Character(0, 10, 100, 10, 0.0, 0.0, 0.0)
    run(char)