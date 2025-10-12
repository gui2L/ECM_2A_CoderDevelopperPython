from grille import Grille

#   Nom : "Plouf dans l'eau"
#   Utilisateur : un joueur
#   Story : On veut pouvoir gérer les tirs de l'adversaire

#   Actions :

#1. créer une grille à 5 lignes et 8 colonnes
g = Grille(5, 8)

#(5.)
while True:
    #2. afficher la grille à l'écran
    g.afficher()

    #3. demande à l'utilisateur de rentrer deux coordonnées x et y
    while True:
        try:
            x, y = map(int, input("Entrez les coordonnées x et y séparées par un espace : ").split())
            break  
        except ValueError:
            print("Saisie invalide ! Veuillez entrer deux nombres séparés par un espace.")

    #4. tirer à l'endroit indiqué sur la grille
    g.tirer(x, y)

    #5. retour en 2
