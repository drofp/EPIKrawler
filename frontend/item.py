#/usr/bin/env python3.6

"""
Parent class for all items

Possible Items: weapons, potions, armor.
"""

class Item(object):
    def __init__(self, sprite, hitboxWidth, hitboxHeight, range):
        self.sprite = sprite
        self.hitboxWidth = hitboxWidth
        self.hitboxHeight = hitboxHeight
