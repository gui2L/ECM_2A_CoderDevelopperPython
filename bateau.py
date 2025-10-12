class Bateau:


    def __init__(self, ligne, colonne, longueur = 1, vertical = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        positions = []
        if self.vertical:
            for i in range(self.longueur):
                positions.append((i+self.ligne, self.colonne))
        else:
            for j in range(self.longueur):
                positions.append((self.ligne, self.colonne+j))
        return positions