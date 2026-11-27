from typing import Any
from Item import Item


class consumable(Item):
    def __init__(self, name: str, item_type: str, description: str, droprate: int, rarity: str, effect: dict):
        super().__init__(name, item_type, description, droprate, rarity, 0, 0)
        self.effect = effect

    def to_dict(self):
        return vars(self).copy()

    def use(self, target: Any):
        for stat, value in self.effect.items():
            if stat == "hp":
                target.heal(value)


