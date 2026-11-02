#importer les données de la base de donnée
#(from pymongo import MongoClient ) etc...

#jeu infinis
#lancement du jeu
#afficher le menu a choix 
#initialiser la list equipe avec rien a l'interieur 

#le menu : 
# afficher nouvelle partie / leaderboard / quit
# demander un choix valide au joueur
# lancer le choix du joueur 

#nouvelle partie
# demande un pseudo 
# lancer choix de l'équipe 
# lance le jeu 

#fonctionalité de choix de l'équipe
# tant que la taille de la list equipe < 3
#   afficher la liste de l'équipe 
#   afficher la liste des heros de la base de donnée
#   demander un choix valide de hero (input)
#      ajouter le choix de hero dans une list equipe
#       l'enlever de la list afficher

# choix valide( number, min, max)
#   boucle
#   choisir un nombre
#     si "" est un nombre (isdigit) et qu'il est entre le min et max 
#         retourner vrais
#     sinon demander de choisir un autre ""


#le jeu fait une boucle
# tant que liste de hero en vie est vrais
#   si le leng de la list hero est égale a 0
#      fin du jeu
#   sinon lancer un tour avec les heros en vie 
# fin du jeu

#fonctionalité de fin du jeu
#  afficher nombre de tour survécue
#     sauvegarder le nombre de tour + le pseudo dans la base de donnée leaderboard
#   on clear la list equipe 

#fonctionnement d'un tour
#initialisation de la list herro en vie 
# hero en vie sont les héros en vie dans l'équipe donc pc>0 
#   si pv d'un hero en vie tombe a <= 0 alors le hero en question est enlevé de la list 
# boucle
# pour chaque hero dans hero en vie 
# on fait attaquer le hero
#  si pv du monstre > 0
#   on fait attaquer le monstre sur un héro aleatoire dans la list des hero en vie

#attaque sera dans les class
#  attaque
#    

#fonctionalité de leaderboard 
#afficher les meilleurs score optenue

#les meilleurs scores optenue sont trié
# les 10 meilleurs sont gardée avec le pseudo choisi 

#fonctionnalité de quit
#afficher "à la prochaine :D"
#fermer le jeu 
