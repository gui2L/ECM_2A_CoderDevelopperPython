from grille import Grille
from bateau import *

def test_Grille_init():
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


def test_Grille_affichage(capsys):
    g = Grille(5, 8)

    g.afficher()
    print(g)

    output = capsys.readouterr().out
    assert Grille.vide in output

    s = str(g)
    assert isinstance(s, str)
    assert s.count(Grille.vide) == 5 * 8



def test_Grille_tirer():
    g = Grille(5, 8)

    error1 = g.tirer(-1, 0)
    assert error1 == -1

    error2 = g.tirer(30, 20)
    assert error2 == -1

    t1 = g.tirer(0, 0)
    t2 = g.tirer(3, 6)
    t3 = g.tirer(5, 8)

    assert t1 == 0
    assert t2 == (3)*g.nombre_colonnes+(6)
    assert t3 == -1

def test_Grille_ajoute():
    

    g1 = Grille(2, 3)

    vide = g1.vide
    icon_bat = g1.icon_bat
    touche = g1.touche

    ajout1 = g1.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert(ajout1 == True)
    assert(g1.matrice == [vide, vide, vide, icon_bat, icon_bat , vide])

    g2 = Grille(2, 3)
    ajout2 = g2.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    ajout3 = g2.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    
    assert(ajout2 == False)
    assert(ajout3 == False)
    assert(g2.matrice == [vide, vide, vide, vide, vide, vide])

def test_Grille_ajoute_bateau_specifique():

    g = Grille(5, 8)

    PorteAvion1 = Porte_avion(0, 8, True)
    Torpilleur1 = Torpilleur(0, 3)
    Sous_marin1 = Sous_marin(3, 2, True)
    Croiseur1 = Croiseur(7, 8)

    g.ajoute(PorteAvion1)
    g.ajoute(Torpilleur1)
    g.ajoute(Sous_marin1)
    g.ajoute(Croiseur1)