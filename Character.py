from Entity import Entity
from Item import Item
from typing import List

class Character(Entity):
    def __init__(self, name: str, hp: int, defense: int, attack: int, equipement: List[Item]):
        super().__init__(name, hp, defense, attack)
        self.equipement = equipement

    def __dict__(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "defense": self.defense,
            "attack": self.attack,
            "equipement": [item.name for item in self.equipement]
        }

    def list_equipement(self):
        return [item.name for item in self.equipement]
    
    @property
    def attack(self):
        total_attack = super().attack
        for item in self.equipement:
            total_attack += item.attack_bonus
        return total_attack

    @property
    def defense(self):
        total_defense = super().defense
        for item in self.equipement:
            total_defense += item.defense_bonus
        return total_defense
    

    def EquipItem(self, item: "Item"):
        self.equipement.append(item)

    def UnequipItem(self, item: "Item"):
        if item in self.equipement:
            self.equipement.remove(item)

    def IsSlotAvailable(self, item: "Item") -> bool:
        if len(self.equipement) < 4 or item not in self.equipement:  # Assuming a maximum of 4 items can be equipped not the same type of item can be equipped at the same time
            return True
        return False  # Placeholder implementation

    def getequipement(self) -> List[Item]:
        return self.equipement

    def projectdamage(self, target: "Entity") -> int:
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        return damage

    def Playturn(self, target: "Entity"):
        self.attack(target)
