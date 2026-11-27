from player import Player
from Vague import Vague
import Enemy
import equipable


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
        self.player.equipe = [Enemy(**monster) for monster in gestionnaire['equpe']]
        self.vague.enemies = [Enemy(**monster) for monster in gestionnaire['monsters']]
        self.player.inventory = [equipable(**item) for item in gestionnaire['inventaire']]

    def lancer_jeu(self, db):
        #lancer le jeu sans sauvegarde
        player = Player("Player1", 100, 10, 20)
        vague = Vague("Vague1", [], 1)
        mongo_client = db
        game = Game(player, mongo_client, vague)
        return game

    def ShowLeaderboard(self):
        leaderboard = self.mongo_client.get_leaderboard()
        for entry in leaderboard:
            print(f"Player: {entry['player_name']}, Score: {entry['score']}")

        
    def Exit(self):
        self.mongo_client.close()
