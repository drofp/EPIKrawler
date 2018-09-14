# Author Vinh Truong

import pickups
import pygame
import time

MOVE_UP = pygame.K_w
MOVE_LEFT = pygame.K_a
MOVE_DOWN = pygame.K_s
MOVE_RIGHT = pygame.K_d

ATTACK = pygame.K_j

tick = 0.01 # length of tick in sec

class characterLogic(object):

    def __init__(self, speed, attack: int, health: int, resistance: int, crit: float, x:float, y:float, max_speed=0.25):
        self.speed = speed
        self.max_speed = max_speed
        self.attack = attack
        self.health = health
        self.dmg_res = resistance
        self.crit = crit
        self.weapon = None
        self.x, self.y = x, y
        self.move_cooldown = time.time() + tick
        self.attack_cooldown = time.time() + tick
        

    ################## INTERACTION ###################

    def shoot(self, direction: (int, int)):
        # Stage will be 400height x 700width
        if self.weapon == None:
            # Attack will be 30 width x 50 length
            pass

    
    def move(self, row_direction, col_direction):
        """
        Primitive movement system, sets the player velocity to the max
        velocity
        """
        if self.move_cooldown > time.time():
            pass

        self.move_cooldown += tick
        self.speed = self.max_speed
        self.x += self.speed*tick*row_direction
        self.y += self.speed*tick*col_direction

    
    def move_stop(self):
        """
        Primitive movement stop, sets player velocity to 0
        """
        self.speed = 0
    


    ################## GET METHODS ###################

    def get_speed(self) -> int:
        return self.speed
    
    def get_attack(self) -> int:
        return self.attack

    def get_health(self) -> int:
        return self.health
    
    def get_resistance(self) -> int:
        return self.dmg_res
    
    def get_crit(self) -> int:
        return self.crit

    ################## SET METHODS ####################

    def set_speed(self, new_speed: int):
        self.speed = new_speed

    def set_attack(self, new_attack: int):
        self.attack = new_attack
    
    def set_health(self, new_health: int):
        self.health = new_health
    
    def set_resistance(self, new_resist: int):
        self.dmg_res = new_resist
    
    def set_crit(self, new_crit: int):
        self.crit = new_crit