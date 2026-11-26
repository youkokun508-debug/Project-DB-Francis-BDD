from Item import Item

class Equipable(Item):
     def __init__(self, name: str,item_type: str, description: str, droprate: int, rarity: str, attack_bonus: int, defense_bonus: int):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.droprate = droprate
        self.rarity = rarity
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
