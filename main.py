#importer les données de la base de donnée
#(from pymongo import MongoClient ) etc...

# jeu infinis
#   afficher le menu a choix 

#initialiser la list equipe avec rien a l'interieur 

#le menu : 
# afficher nouvelle partie / leaderboard / quit
# demander un choix valide au joueur
# lancer le choix valide du joueur 

#nouvelle partie
# demande un pseudo 
# lancer choix de l'équipe 
# lance le jeu 

#fonctionalité de choix de l'équipe
# initialiser la list "list des heros de la base"
# tant que la taille de la list equipe < 3
#   afficher la liste de l'équipe 
#   afficher la liste des heros de la base de donnée 
#   demander un choix valide de hero (input)
#      ajouter le choix de hero dans une list equipe
#       enlever le hero choisi de la list des heros de la base de donnée

# demander choix valide(number, min, max)
#   boucle
#   le joueur choisi un nombre
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
#   afficher nombre de tour survécue
#   si le nombre de tour survécue est valide (dans le top 10)
#       on supprime la première sauvegarde de tour et son pseudo de la base de donnée
#       sauvegarder le nombre de tour + le pseudo dans la base de donnée leaderboard
#       on trie la list dans l'ordre croissant 
#   on clear la list equipe 

#monstre = un monstre aléatoire dans la list monstre

#initialisation de la list herro en vie
# hero en vie sont les héros en vie dans l'équipe donc 
#   si pv d'un hero en vie tombe a <= 0 alors le hero en question est enlevé de la list 

#fonctionnement d'un tour
# boucle
# pour chaque hero dans la list hero en vie 
# on fait attaquer un herro en vie
#  si pv du monstre > 0 
#   on fait attaquer le monstre (sur un héro aleatoire dans la list des hero en vie)

#tour sera dans les class (hunter, target)
#  target subie des degats du hunter

#tour du monstre sera dans la class monstre(hunter, taget)
#   target choisi au hazard vas subir des dégats du hunter

#subir dégat(charecter, hunter)
#   pv(character) - dégat
#   actualise les pv(character)

# calcule dégat(charactere, hunter)
#     att(hunter) - calcule defence
#     si att(hunter) < 0 
#          retourner att(hunter)
#     sinon
#         att(hunter) = 1
#         retourner int(att(hunter))

# calcule defence
#   si il a des items
#       def + def items
#       retourner def
#   sinon
#       retourner def


#fonctionalité de leaderboard 
#afficher les meilleurs score optenue

#les meilleurs scores optenue sont trié
# les 10 meilleurs sont gardée avec le pseudo choisi 

#fonctionnalité de quit
#afficher "à la prochaine :D"
#fermer le jeu 
