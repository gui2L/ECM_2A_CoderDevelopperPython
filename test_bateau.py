from bateau import Bateau 

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