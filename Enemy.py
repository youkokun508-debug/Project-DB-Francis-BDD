from Entity import Entity
from Item import Item
from typing import List
import random

class Enemy(Entity):
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
        lacher = []
        for item in self.dropable:
            if self.sa_drop():
                lacher.append(item)
        return lacher

    def PlayTurn(self, target: "Entity"):
        return self.attack(random.choice([enemy for enemy in self.enemies if enemy != target]))

    def sa_drop(self) -> bool:
        return random.choice([True, False])