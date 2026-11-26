from Entity import Entity
from Item import Item
from typing import List

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
        # Placeholder implementation - replace with actual item dropping logic
        return self.dropable

    def PlayTurn(self, target: "Entity"):
        # Here you can implement the logic for the monster's turn
        self.attack(target)