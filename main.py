#importer les données de la base de donnée
#(from pymongo import MongoClient ) etc...


#jeu infinis
#afficher le menu a choix 

#le menu : 
# afficher nouvelle partie / leaderboard / quit
# choix valide du joueur
# si choix du joueur est valide 
# lancer le choix du joueur 

#nouvelle partie
# demande un pseudo
# choix de l'équipe 
# lance le jeu 

#fonctionalité de choix de l'équipe
# tant que la taille de la list equipe différent de 3
#   afficher la liste des heros
#   faire un choix valide de hero (input)
#      ajouter le choix de hero dans une list equipe
#       l'enlever de la list afficher

# choix valide( number, min, max)
#   boucle
#   choisir un nombre
#     si "" est un nombre (isdigit) et qu'il est entre le min et max 
#         retourner vrais
#     sinon demander de choisir un autre ""


#le jeu fait une boucle
# tant que equipe est en vie
#   lancer un tour
# fin du jeu

#fonctionalité de fin du jeu
#  afficher nombre de tour survécue
#     sauvegarder le nombre de tour + le pseudo dans la base de donnée leaderboard

#fonctionnement des tours
#   si hero en vie est vrais
#       tour hero
#           attaque (hero)
#   si monstre en vie est vrais
#     tour monstre
#           attaque (monstre)

# fonctionalité de "" est en vie
#   si pv <=0
#       retourner faux
#   retourner vrais

#attaque sera dans les class
#   

#fonctionalité de leaderboard 
#afficher les meilleurs score optenue

#les meilleurs scores optenue sont trié
# les 10 meilleurs sont gardée avec le pseudo choisi 

#fonctionnalité de quit
#afficher "à la prochaine :D"
#fermer le jeu 
