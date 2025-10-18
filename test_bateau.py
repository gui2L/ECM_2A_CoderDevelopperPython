from bateau import Bateau 
from grille import Grille

def test_Bateau_init():
    
    b1 = Bateau(ligne=2, colonne=3, longueur=4, vertical=True)
    assert b1.ligne == 2
    assert b1.colonne == 3
    assert b1.longueur == 4
    assert b1.vertical is True

    b2 = Bateau(1, 2)
    assert b2.ligne == 1
    assert b2.colonne == 2
    assert b2.longueur == 1     # valeur par défaut
    assert b2.vertical is False # valeur par défaut


def test_Bateau_positions():
    assert Bateau(2, 3, longueur=3).positions == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions == [(2, 3), (3, 3), (4, 3)]

def test_Bateau_chevauche():
    b1 = Bateau(2, 3, 4)
    b2 = Bateau(1, 4, 2, True)
    b3 = Bateau(3, 5, 4)
    b4 = Bateau(3, 5, 4)
    assert(b1.chevauche(b2))
    assert(not b2.chevauche(b3))
    assert(not b1.chevauche(b3))
    assert(b4.chevauche(b3))
     
def test_Bateau_coulé():
    g = Grille(5, 8)

    b1 = Bateau(2, 3, 4)
    b2 = Bateau(1, 4, 2, True)
    b3 = Bateau(3, 5, 4)
    b4 = Bateau(3, 5, 4)

    g.ajoute(b1)
    g.ajoute(b2)
    g.ajoute(b3)
    g.ajoute(b4)

    g.tirer(1, 4)
    g.tirer(2, 4)
    assert(b2.coulé(g) == True)
    assert(b3.coulé(g) == False)

