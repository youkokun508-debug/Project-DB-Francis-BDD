
class Entity:
    def __init__(self, name: str, hp: int, defense: int, attack: int):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack

    def __dict__(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "defense": self.defense,
            "attack": self.attack
        }

    def IsAlive(self) -> bool:
        return self.hp > 0


    def TakeDamage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount: int):
        self.hp += amount

    def Attack(self, target: "Entity"):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        target.TakeDamage(damage)

    def PlayTurn(self, target: "Entity"):
        self.Attack(target)
