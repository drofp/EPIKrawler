# Author Vinh Truong

import Pickups

class Character(object):
    def __init__(self, speed: int, attack: int, health: int, resistance: int, crit: float, position: (int, int)):
        self.speed = speed
        self.attack = attack
        self.health = health
        self.dmg_res = resistance
        self.crit = crit
        self.weapon = None
        self. position = position
    ################## INTERACTION ###################

    def shoot(self, direction: (int, int)):
        # Stage will be 400height x 700width
        if self.weapon == None:
            # Attack will be 30 width x 50 length
            pass

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