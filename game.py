class game:
    def __init__(self, player_name: str, mongodb: "MongoDB", vague: int):
        self.player_name = player_name
        self.mongodb = mongodb
        self.vague = vague

    