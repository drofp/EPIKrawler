#!/usr/bin/env python3.6

import pygame
from pygame.locals import *

import colors

class CharacterDisplay(pygame.sprite.Sprite):
    """
    Parent class for all characters.

    Possible Characters: Player, enemies

    References:
    http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
    http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
    """

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

        self.rectChar = rectChar
        self.x = startX
        self.y = startY
        self.hitboxWidth = hitboxWidth
        self.hitboxHeight = hitboxHeight
        self.deltaX = deltaX
        self.deltaY = deltaY

        if self.rectChar:
            pygame.draw.rect(screen, colors.GREEN, [self.x, self.y, self.hitboxWidth, self.hitboxHeight])

        self.image = pygame.Surface([hitboxWidth, hitboxHeight])

    def update_loc(self, screen):
        """Updates location of character for display.
        """

        screenW, screenH = screen.get_size()

        # TODO: stop at edge of screen
        if self.x + self.hitboxWidth + self.deltaX > screenW or self.x + self.deltaX < 0:
            self.deltaX = 0
        if self.y + self.hitboxHeight + self.deltaY > screenH or self.y + self.deltaY < 0:
            self.deltaY = 0

        self.x += self.deltaX
        self.y += self.deltaY

        if self.rectChar:
            pygame.draw.rect(screen, colors.GREEN, [
                             self.x, self.y, self.hitboxWidth, self.hitboxHeight])
