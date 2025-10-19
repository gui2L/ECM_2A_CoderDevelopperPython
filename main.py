from grille import Grille
from bateau import *

def main():
    g = Grille(8, 10)
    types_bateau = [Porte_avion, Croiseur, Torpilleur, Sous_marin]
    for type in types_bateau:
        g.placer_aleatoirement(type)
    
    play = 1
    while play != -1:
        print(g)
        while True:
            try:
                x, y = map(int, input("Entrez les coordonnées x et y séparées par un espace : ").split())
                break  
            except ValueError:
                print("Saisie invalide ! Veuillez entrer deux nombres séparés par un espace.")
        play = g.tirer(x-1, y-1)
    
    return 0



if __name__ == "__main__":
    main()