class Grille:
    vide = "~"


    def __init__(self, nombre_lignes=0, nombre_colonnes=0):
        self.matrice = [Grille.vide*nombre_colonnes*nombre_lignes]
        self.nombre_colonnes = nombre_colonnes
