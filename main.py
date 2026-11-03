#importer toute ma bdd et l'initialiser 


#initialiser le jeu 
# boucle infini
#   afficher le menu
#   demande un choix valide
#   executer le choix valide 

#afficher le menu
#   1/ nouvelle partie
#   2/ Leaderboard
#   3/ Quitter le jeu

#demander un choix valide
#   demander un choix input
#       si choix est valide(choix, min, max)
#           retourner choix
#       sinon
#           demander un autre choix input

#verifier le choix valide(choix, min, max)
# boucle infini
#   si choix n'est pas un nombre isdigit
#       retourner false
#   si choix < min et choix > max 
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
#   recuperer l'equipe TODO:
#   lancer un jeu TODO:
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
#   initialise l'equipe en vie 
#   boucle tant que taille de equipe > 3 
#      choix de l'equipe TODO:
#   equipe en vie = equipe
#   return equipe

#choix de l'equipe
#       afficher l'equipe 
#       afficher les heros dispo
#       demander un choi valide de hero (input) TODO:
#       ajouter la choix de hero dans une list equipe
#       enlever le hero choisi de la list des heros de la base de donnée