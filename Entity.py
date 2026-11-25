from dataclasses import dataclass
from typing import Dict, List

class Entity:
    def __init__(self, name: str, hp: int, defense: int, attack: int):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack

    def __dict__(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "defense": self.defense,
            "attack": self.attack
        }

    def IsAlive(self) -> bool:
        return self.hp > 0


    def TakeDamage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount: int):
        self.hp += amount

    def Attack(self, target: "Entity"):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        target.TakeDamage(damage)

    def Playturn(self, target: "Entity"):
        self.Attack(target)

class Character(Entity):
    def __init__(self, name: str, hp: int, defense: int, attack: int, equipement: List["Item"]):
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
        # Here you can implement the logic to check if the character has an available slot for the item
        # For example, you can limit the number of items a character can equip
        return True  # Placeholder implementation

    def getequipement(self) -> List["Item"]:
        return self.equipement

    def projectdamage(self, target: "Entity") -> int:
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        return damage

    def Playturn(self, target: "Entity"):
        # Here you can implement the logic for the character's turn
        # For example, you can choose to attack or use an item
        self.Attack(target)

class Monster(Entity):
    def __init__(self, name: str, hp: int, defense: int, attack: int, dropable: List["Item"]):
        super().__init__(name, hp, defense, attack)
        self.dropable = dropable

    def __dict__(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "defense": self.defense,
            "attack": self.attack,
            "dropable": [item.name for item in self.dropable]
        }

    def list_dropable(self):
        return [item.name for item in self.dropable]

    def DropItem(self) -> List["Item"]:
        # Here you can implement the logic to determine which items the monster drops
        # For example, you can randomly select items from the dropable list
        return self.dropable  # Placeholder implementation

    def PlayTurn(self, target: "Entity"):
        # Here you can implement the logic for the monster's turn
        self.Attack(target)