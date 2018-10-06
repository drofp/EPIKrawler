#!/usr/bin/env python3.6

import pygame
import colors

# References: 
# http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
# http://programarcadegames.com/python_examples/f.php?file=platform_moving.py

"""
Parent class for all characters.

Possible Characters: Player, enemies
"""

class CharacterDisplay(pygame.sprite.Sprite):
    """For creating and displaying characters."""
    def __init__(self, screen, startX=0, startY=0, hitboxWidth=100, hitboxHeight=100, rectChar=False):
        """Creates a character object.
        
        This includes players and NPC's.
        
        Setting 'rectChar' to True will instantiate a character as a rectangle."""

        pygame.sprite.Sprite.__init__(self)

        # TODO: Add in instance var and sprite mode
        # self.sprite = sprite

        self.x = startX
        self.y = startY
        self.hitboxWidth = hitboxWidth
        self.hitboxHeight = hitboxHeight

        if rectChar:
            pygame.draw.rect(screen, colors.GREEN, [self.x, self.y, self.hitboxWidth, self.hitboxHeight])

        self.image = pygame.Surface([hitboxWidth, hitboxHeight])

    def update(self, event):
        """
        Updates position of character.

        Uses logic from backend.
        """

        pass

        
        



