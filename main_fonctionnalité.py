from grille import Grille
from bateau import *

def main():
    
    g = Grille(5, 8)
    
    g.afficher()
    print(g)
    print()

    b1 = Bateau(2, 3, 4)
    b2 = Bateau(1, 4, 2, True)
    b3 = Bateau(3, 5, 4)
    b4 = Bateau(3, 5, 9)
    g.ajoute(b1)
    g.ajoute(b2)
    g.ajoute(b3)
    g.ajoute(b4)
    print(g)

    g.tirer(1, 4)
    g.tirer(2, 4)
    print(g)

    print(b2.coulé(g))
    print(b3.coulé(g))

    PorteAvion1 = Porte_avion(0, 7, True)
    print(PorteAvion1.marque)

    Torpilleur1 = Torpilleur(0, 3)
    print(Torpilleur1.marque)

    g.ajoute(PorteAvion1)
    g.ajoute(Torpilleur1)

    print(g)
    print()

    g = Grille(4, 4)

    PorteAvion1 = Porte_avion(0, 0)
    Torpilleur1 = Torpilleur(1, 0)
    Sous_marin1 = Sous_marin(2, 0)
    Croiseur1 = Croiseur(3, 0)

    ajout1 = g.ajoute(PorteAvion1)
    ajout2 = g.ajoute(Torpilleur1)
    ajout3 = g.ajoute(Sous_marin1)
    ajout4 = g.ajoute(Croiseur1)

    print(g)
    return 0

if __name__ == "__main__":
    main()