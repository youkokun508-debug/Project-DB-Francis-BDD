class vague:
    def __init__(self, name: str, enemies: list["Monster"], difficulty: int):
        self.name = name
        self.enemies = enemies
        self.difficulty = difficulty

    def vague__actuel(self):
        return {
            "name": self.name,
            "enemies": [enemy.name for enemy in self.enemies],
            "difficulty": self.difficulty
        }
    def list_enemies(self):
        return [enemy.name for enemy in self.enemies]
    def PickEnemies(self) -> list["Monster"]:
        # Here you can implement the logic to determine which enemies are picked for the vague
        # For example, you can randomly select enemies from the enemies list based on difficulty
        return self.enemies  # Placeholder implementation
    def PlayTurn(self, target: "Entity"):
        # Here you can implement the logic for the vague's turn
        for enemy in self.enemies:
            enemy.PlayTurn(target)
    def Getdifficulty(self):
        return self.difficulty
    