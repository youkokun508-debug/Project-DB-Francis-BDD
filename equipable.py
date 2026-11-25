class Equipable(Item):
    def __init__(self, name: str, item_type: str, description: str, droprate: int, rarity: str, attack_bonus: int, defense_bonus: int):
        super().__init__(name, item_type, description, droprate, rarity, attack_bonus, defense_bonus)
