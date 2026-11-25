
class Character(Entity):
    def __init__(self, name: str, hp: int, defense: int, attack: int, equipement: List["Item"]):
        super().__init__(name, hp, defense, attack)
        self.equipement = equipement

    def __dict__(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "defense": self.defense,
            "attack": self.attack,
            "equipement": [item.name for item in self.equipement]
        }

    def list_equipement(self):
        return [item.name for item in self.equipement]
    
    @property
    def attack(self):
        total_attack = super().attack
        for item in self.equipement:
            total_attack += item.attack_bonus
        return total_attack

    @property
    def defense(self):
        total_defense = super().defense
        for item in self.equipement:
            total_defense += item.defense_bonus
        return total_defense
    

    def EquipItem(self, item: "Item"):
        self.equipement.append(item)

    def UnequipItem(self, item: "Item"):
        if item in self.equipement:
            self.equipement.remove(item)

    def IsSlotAvailable(self, item: "Item") -> bool:
        # Here you can implement the logic to check if the character has an available slot for the item
        # For example, you can limit the number of items a character can equip
        return True  # Placeholder implementation

    def getequipement(self) -> List["Item"]:
        return self.equipement

    def projectdamage(self, target: "Entity") -> int:
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        return damage

    def Playturn(self, target: "Entity"):
        # Here you can implement the logic for the character's turn
        # For example, you can choose to attack or use an item
        self.Attack(target)
