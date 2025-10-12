from grille import Grille

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
    return 0

if __name__ == "__main__":
    main()