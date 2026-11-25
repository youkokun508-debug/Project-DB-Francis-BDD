
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