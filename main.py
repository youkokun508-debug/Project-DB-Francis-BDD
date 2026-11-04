#importer toute ma bdd et l'initialiser 


#initialiser le jeu 
# boucle infini
#   afficher le menu
#   recuperer un choix valide
#   executer le choix valide 

#afficher le menu
#   1/ nouvelle partie
#   2/ Leaderboard
#   3/ Quitter le jeu

#recuperer un choix valide
#   demander un choix input
#       si choix est valide(choix, min, max)
#           retourner choix
#       sinon
#           demander un autre choix input

#verifier le choix valide(choix, min, max)
# boucle infini
#   si choix n'est pas un nombre isdigit
#       retourner false
#   si choix < min ou choix > max 
#       retourner false
#    retourner vrais

#executer le choix valide
#   si le choix = 1 
#       lancer une nouvelle partie
#   si le choix = 2
#       ouvrir le leaderboard
#   si le choix = 3
#       Fermer le jeu

#Lancer une nouvelle partie
#   recuperer le pseudo
#   recuperer l'equipe
#   lancer le jeu 

#ouvrir le leaderboard
#   afficher la list leaderboard par le dernier (car list trié ordre croissant du score)

#recuperer le pseudo valide
#   demande de rentrer le pseudo input
#   si le peudo est valide
#       retourner le pseudo
#   sinon 
#       redemander de rentrer un pseudo valide 

#le pseudo valide 
#   si le peudo n'est pas des lettre (isidentifier)
#       return false    
#   sinon 
#       return true 

#recuperer l'equipe 
#   initialise l'equipe avec rien
#   recuperer heros dispo epuis la b 
#   boucle tant que taille de equipe < 3 
#      choix de l'equipe
#   return equipe

#choix de l'equipe
#       afficher l'equipe 
#       afficher les heros dispo
#       recuperer un choix valide
#       ajouter la choix de hero dans une list equipe inex = choix - 1 
#       enlever le hero choisi de la list des heros dispo

#lancer le jeu
#boucle infini
#   tant que equipe en vie
#       gerer l'apparition du monstre en vie
#       lancer un tour
#   enregistre le score optenue
#   fin du jeu 

#enregistre le score optenue 
#   si la liste leaderboard < 10
#       ajouter le score + pseudo dans la liste
#   sinon
#       si score dans le top 10 
#           supprimer le premier score + pseudo de la list 
#           ajoute le score + pseudo dans la liste
#           trie la list dans l'ordre croissant 

#score dans le top 10
#   si le score > au premier score 
#       retourner vrais
#   sinon 
#       retourner faux

#fin du jeu
#   message de fin du jeu
#   ferme le jeu

#lancer un tour
#   pour chaque hero dans equipe qui est en vie 
#       si pv monstre en vie > 0
#           tour (hero)
#   si pv monstre en vie > 0 et si equipe en vie 
#       tour (monstre) 

#en vie
#   pour chaque personnage dans equipe 
#       si pv du personnage > 0
#           retourne vrais
#       sinon
#           retourner faux

#gerer l'apparition du monstre en vie
#   si il n'y a rien dans monstre en vie
#       on ajoute un monstre au hasard dans monstre en vie
#   sinon
#       si les pv du monstre en vie sont > 0
#           pass
#       sinon
#           on supprime le monstre (pop)
#           on ajoute un monstre au hasard dans monstre en vie

#tour hero sera dans les class (hunter, target)
#  target subie des degats du hunter

#tour du monstre sera dans la class monstre(hunter, taget)
#   target choisi au hazard vas subir des dégats du hunter

#subir dégat(charecter, hunter)
#   actualise les pv(character, calcule degats) 
#   retourner pv charactere

#actualiser les pv 
#   pv(character) -= calcule dégats
#   retourner les pv

#calcule degats(hunter, cible)
#   degats = att(hunter) - calcule defence
#   si degats < 1
#       degats = 1
#   retourner degats

#calcule defense(self)
#   retourner defense + somme des defenses des items 

#somme des defences des items
#   pour chaque item dans la liste item 
#       on ajoute les def de chaque item ( sum(item[def]) )