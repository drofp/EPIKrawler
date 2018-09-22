#!/usr/bin/env python3.6

import pygame

# References: 
# http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
# http://programarcadegames.com/python_examples/f.php?file=platform_moving.py

"""
Parent class for all characters.

Possible Characters: Player, enemies
"""


class CharacterDisplay(pygame.sprite.Sprite):
    def __init__(self, sprite, hitboxWidth, hitboxHeight):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = sprite
        self.hitboxWidth = hitboxWidth
        self.hitboxHeight = hitboxHeight

        self.image = pygame.Surface([hitboxWidth, hitboxHeight])

        self.walls = None

    def update(self):
        """
        Updates position of character.

        Uses logic from backend.
        """
        return


