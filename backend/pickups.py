# Author Vinh Truong

from items import item

class weapon(item):
    def __init__(self, name: str, picture: 'picture', melee: bool, damage: int):
        super.__init__(name, picture)
        self.melee = melee
        self.damage = damage

class passive(item):
    def __init__(self, name:str, picture: 'picture', effect: "function"):
        super.__init__(name, picture)
        self.effect = effect
    
