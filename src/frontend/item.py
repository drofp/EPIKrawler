#/usr/bin/env python3.6

import pygame

"""
Parent class for all items

Possible Items: weapons, potions, armor.
"""


class ItemDisplay(pygame.sprite.Sprite):
    def __init__(self, sprite, hitboxWidth, hitboxHeight, range):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = sprite
        self.hitboxWidth = hitboxWidth
        self.hitboxHeight = hitboxHeight

        self.image = pygame.Surface([hitboxWidth, hitboxHeight])

    def update(self):
        """
        Updates position of item.

        Uses logic from backend.
        """

        return
