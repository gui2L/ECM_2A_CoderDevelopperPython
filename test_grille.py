from grille import Grille

def test_init():
    g = Grille() # grille 4x4 par defaut choisie personnellement 
    assert g.nombre_lignes == 4
    assert g.nombre_colonnes == 4
    assert len(g.matrice) == 4*4


    g1 = Grille(0, 0) 
    assert g1.nombre_lignes == 0
    assert g1.nombre_colonnes == 0
    assert len(g1.matrice) == 0

    g2 = Grille(5, 8)
    assert g2.nombre_lignes == 5
    assert g2.nombre_colonnes == 8
    assert len(g2.matrice) == 5 * 8

    g3 = Grille(1)
    assert g3.nombre_lignes == 1
    assert g3.nombre_colonnes == 4
    assert len(g3.matrice) == 4


def test_affichage(capsys):
    g = Grille(5, 8)

    g.afficher()
    print(g)

    output = capsys.readouterr().out
    assert "~" in output

    s = str(g)
    assert isinstance(s, str)
    assert s.count("~") == 5 * 8



def test_tirer():
    g = Grille(5, 8)

    error1 = g.tirer(0, 0)
    assert error1 == -1

    error2 = g.tirer(30, 20)
    assert error2 == -1

    t1 = g.tirer(1, 1)
    t2 = g.tirer(3, 6)
    t3 = g.tirer(5, 8)

    assert t1 == 0
    assert t2 == (3-1)*g.nombre_colonnes+(6-1)
    assert t3 == 39