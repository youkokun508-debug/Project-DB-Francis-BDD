import random
import Enemy
import Entity
import player
import equipable
import consumable

class Vague:
    def __init__(self, name: str, enemies: list["Enemy"], difficulty: int):
        self.name = name
        self.enemies = enemies
        self.difficulty = difficulty

#    def vague__actuel(self):


        
    def list_enemies(self):
        return [enemy.name for enemy in self.enemies]
    def PickEnemies(self) -> list["Enemy"]:
        return self.enemies
       
    def PlayTurn(self, target: "Entity"):
        # Here you can implement the logic for the vague's turn
        for enemy in self.enemies:
            enemy.PlayTurn(target)

    def Getdifficulty(self):
        lap_fait = 0
        if self.vague__actuel() is not None:
            lap_fait += 1

        return self.difficulty