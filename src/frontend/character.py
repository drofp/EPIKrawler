#!/usr/bin/env python3.6

import pygame
import colors

"""
Parent class for all characters.

Possible Characters: Player, enemies

References: 
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
"""

class CharacterDisplay(pygame.sprite.Sprite):
    """For creating and displaying characters."""

    def __init__(self, screen, rectChar=False, startX=0, startY=0, hitboxWidth=100, hitboxHeight=100, 
                        deltaX=0, deltaY=0):
        """
        Creates a character object.
        
        This includes players and NPC's.
        
        Setting 'rectChar' to True will instantiate a character as a rectangle.
        """

        pygame.sprite.Sprite.__init__(self)

        # TODO: Add in instance var and sprite mode
        # self.sprite = sprite

        self.x = startX
        self.y = startY
        self.hitboxWidth = hitboxWidth
        self.hitboxHeight = hitboxHeight

        self.deltaX = deltaX
        self.deltaY = deltaY

        self.rectChar = rectChar

        if self.rectChar:
            pygame.draw.rect(screen, colors.GREEN, [self.x, self.y, self.hitboxWidth, self.hitboxHeight])

        self.image = pygame.Surface([hitboxWidth, hitboxHeight])

    def update_loc_deltas(self, keysPressed):
        """
        Updates change in position of character.

        Uses logic from backend.
        """

        if keysPressed[pygame.K_LEFT]:
            self.deltaX = -5
        else:
            if keysPressed[pygame.K_RIGHT]:
                self.deltaX = 5
            else:
                self.deltaX = 0

        if keysPressed[pygame.K_UP]:
            self.deltaY = -5
        else:
            if keysPressed[pygame.K_DOWN]:
                self.deltaY = 5
            else:
                self.deltaY = 0

    def update_loc(self, screen):
        """Updates location of character for display."""

        self.x += self.deltaX
        self.y += self.deltaY

        if self.rectChar:
            pygame.draw.rect(screen, colors.GREEN, [
                             self.x, self.y, self.hitboxWidth, self.hitboxHeight])

        
        



