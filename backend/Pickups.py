# Author Vinh Truong

from Items import Item

class Weapon(Item):
    def __init__(self, name: str, picture: 'picture', melee: bool, damage: int):
        super.__init__(name, picture)
        self.melee = melee
        self.damage = damage

class Passive(Item):
    def __init__(self, name:str, picture: 'picture', effect: "function"):
        super.__init__(name, picture)
        self.effect = effect
    
