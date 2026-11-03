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
#   sinon
#       retourner vrais

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
#   lancer le jeu TODO:
#   Fin du jeu TODO: 
#

#ouvrir le leaderboard
#   afficher le leaderboard

#Fermer le jeu
#   ferme le jeu

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
#   boucle tant que taille de equipe < 3 
#      choix de l'equipe
#   return equipe

#choix de l'equipe
#       afficher l'equipe 
#       afficher les heros dispo
#       recuperer un choix valide de hero 
#       ajouter la choix de hero dans une list equipe
#       enlever le hero choisi de la list des heros de la base de donnée

#lancer le jeu
#boucle infini
#   tant que equipe en vie > 0
#       apparition d'un monstre au hasard
#       lancer un tour TODO:
#   fin du jeu TODO:

#lancer un tour
#   affichage
#   pour chaque hero dans equipe en vie
#       si pv monstre en vie > 0
#           attaque (hero) TODO:
#   si pv monstre en vie > 0
#       attaque (monstre) TODO:

#apparition d'un monstre au hasard
#   si il n'y a rien dans monstre en vie
#       on ajoute un monstre au hasard dans monstre en vie
#   sinon
#       si les pv du monstre en vie sont > 0
#           pass
#       sinon
#           on supprime le monstre (pop)
#           on ajoute un monstre au hasard dans monstre en vie     

#