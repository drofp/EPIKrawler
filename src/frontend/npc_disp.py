#!/usr/bin/env python3.6

import pygame
import character_disp

class NPCDisplay(character_disp.CharacterDisplay):
    """
    For all non-player characters (NPC's).
    """

    def __init__(self, screen, rectChar=False, startX=0, startY=0, hitboxWidth=100, hitboxHeight=100,
                 deltaX=0, deltaY=0):
        super().__init__(screen, rectChar=rectChar, startX=startX, startY=startY, hitboxWidth=hitboxWidth,
                         hitboxHeight=hitboxHeight, deltaX=deltaX, deltaY=deltaY)

    def move_pattern_1(self):
        pass
    
    def move_attack_1(self):
        pass

    def move_defend_1(self):
        pass

