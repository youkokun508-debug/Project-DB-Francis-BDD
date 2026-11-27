
class Entity:
    def __init__(self, name: str, hp: int, defense: int, attack: int, max_hp: int = None):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp if max_hp is not None else hp
        self.defense_base = defense
        self.attack_base = attack

    def __dict__(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "defense_base": self.defense_base,
            "attack_base": self.attack_base
        }

    def is_alive(self) -> bool:
        return self.hp > 0


    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            return f"{self.name} has been defeated!"
        else:
            return f"{self.name} took {damage} damage and has {self.hp} HP left."

    def heal(self, amount: int):
        self.hp += self.hp + amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target: "Entity"):
        damage = self.attack_base - target.defense_base
        if damage < 0:
            damage = 0
        target.take_damage(damage)

    def play_turn(self, target: "Entity"):
        return self.attack(target)
