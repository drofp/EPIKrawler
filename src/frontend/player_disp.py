#!/usr/bin/env python3.6

import pygame
from pygame.locals import *

import character_disp

class PlayerDisplay(character_disp.CharacterDisplay):
    """
    For all playable characters.
    """

    def __init__(self, screen, rectChar=False, startX=0, startY=0, hitboxWidth=100, hitboxHeight=100,
                 deltaX=0, deltaY=0):
        super().__init__(screen, rectChar=rectChar, startX=startX, startY=startY, hitboxWidth=hitboxWidth, 
                        hitboxHeight=hitboxHeight, deltaX=deltaX, deltaY=deltaY)

    def update_loc_deltas(self, keysPressed):
        """
        Updates change in position of character.

        TODO: Use logic from backend.
        """

        # TODO: Maybe utilize rect class builtins
        # - https://stackoverflow.com/questions/28702750/my-character-sprite-doesnt-move-off-screen
        # - https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move_ip
        # - https://www.pygame.org/docs/ref/rect.html#pygame.Rect.clamp_ip

        if keysPressed[pygame.K_a] or keysPressed[pygame.K_LEFT]:
            self.deltaX = -5
        else:
            if keysPressed[pygame.K_d] or keysPressed[pygame.K_RIGHT]:
                self.deltaX = 5
            else:
                self.deltaX = 0

        if keysPressed[pygame.K_w] or keysPressed[pygame.K_UP]:
            self.deltaY = -5
        else:
            if keysPressed[pygame.K_s] or keysPressed[pygame.K_DOWN]:
                self.deltaY = 5
            else:
                self.deltaY = 0
    
def main():
    import window
    import colors

    backgroundImg = colors.DARK_BLUE

    testScreenW, testScreenH = 500, 500
    testScreen = pygame.display.set_mode((testScreenW, testScreenH))
    testWindow = window.Window(testScreen, backgroundImg)

    testPlayerW, testPlayerH = 100, 100
    testPlayer = PlayerDisplay(testScreen, startX=testScreenW/2 - testPlayerW/2,
                                      startY=testScreenH/2 - testPlayerH/2, rectChar=True)

    print("testPlayer's hitbox width is:", testPlayer.hitboxWidth)

if __name__ == '__main__':
    main()
