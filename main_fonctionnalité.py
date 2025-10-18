from grille import Grille
from bateau import Bateau

def main():
    
    g = Grille(5, 8)
    
    g.afficher()
    print(g)
    print()

    g.tirer(1, 1)
    g.tirer(2, 1)
    g.tirer(4, 3)
    g.tirer(5, 8)

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
    return 0

if __name__ == "__main__":
    main()