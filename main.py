from grille import Grille
from bateau import *

def main():
    g = Grille(8, 10)
    types_bateau = [Porte_avion, Croiseur, Torpilleur, Sous_marin]
    for type in types_bateau:
        g.placer_aleatoirement(type)

    print(g)
    return 0



if __name__ == "__main__":
    main()