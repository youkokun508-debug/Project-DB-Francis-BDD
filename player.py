from pymongo import MongoClient
from typing import List

mongo_client = MongoClient()
gamedb = mongo_client["gamedb"]
import Character


class Player:
    def __init__(self, name: str, score: int, team: list["Character"], inventory: List["Item"]):
        self.name = name
        self.score = score
        self.team = team
        self.inventory = inventory

    def createteam(self, characters: list["Character"]):
        self.team = characters

    def pickcharacter(self, character_name: str) -> "Character":
        for character in self.team:
            if character.name == character_name:
                return character
        return None

    def isteamalive(self) -> bool:
        return any(character.IsAlive() for character in self.team)

    def checkinventory(self) -> list[str]:
        return [item.name for item in self.inventory]

    def useitem(self, item_name: str, target: "Entity"):
        for item in self.inventory:
            if item.name == item_name:
                if isinstance(item, consumable):
                    item.use(target)
                    self.removeitem(item)
                break

    def additem(self, item: "Item"):
        self.inventory.append(item)

    def removeitem(self, item: "Item"):
        if item in self.inventory:
            self.inventory.remove(item)

    def getteam(self) -> list[str]:
        return [character.name for character in self.team]

    def getinventory(self) -> list[str]:
        return [item.name for item in self.inventory]