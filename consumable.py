class consumable(Item):
    def __init__(self, name: str, item_type: str, description: str, droprate: int, rarity: str, effect: dict):
        super().__init__(name, item_type, description, droprate, rarity, 0, 0)
        self.effect = effect

    def __dict__(self):
        base_dict = super().__dict__()
        base_dict["effect"] = self.effect
        return base_dict

    def use(self, target: "Entity"):
        for stat, value in self.effect.items():
            if stat == "hp":
                target.heal(value)


