from player import Player
from Vague import Vague



class Game:
    def __init__(self, player: "Player", mongo_client: "MongoClient", vague: "Vague"):
        self.player = player
        self.mongo_client = mongo_client
        self.vague = vague

    def save_game(self):
        self.mongo_client.save_game(self.player.to_dict(),
                    self.vague.to_dict(),                    equpe=[monster.to_dict() for monster in self.player.equipe],
                    monsters=[monster.to_dict() for monster in self.vague.enemies],
                    inventaire=[item.to_dict() for item in self.player.inventory],
                    score=self.player.score )
        
    def LoadGame(self):
        gestionnaire = self.mongo_client.load_game()
        self.player = Player(**gestionnaire['player'])
        self.vague = Vague(**gestionnaire['vague'])
        self.player.equipe = [Monster(**monster) for monster in gestionnaire['equpe']]
        self.vague.enemies = [Monster(**monster) for monster in gestionnaire['monsters']]
        self.player.inventory = [Equipable(**item) for item in gestionnaire['inventaire']]

    def lancer_jeu(db):
        #ask name cause its a new game
        name = input("Enter your name: ")
        joueur = creer_joueur(db, name)
        

    def ShowLeaderboard(self):
        leaderboard = self.mongo_client.get_leaderboard()
        for entry in leaderboard:
            print(f"Player: {entry['player_name']}, Score: {entry['score']}")

        
    def Exit(self):
        self.mongo_client.close()
