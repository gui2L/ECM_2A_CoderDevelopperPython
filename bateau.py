class Bateau:


    def __init__(self, ligne, colonne, longueur = 1, vertical = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical



    @property
    def positions(self):
        positions = []
        if self.vertical:
            for i in range(self.longueur):
                positions.append((i+self.ligne, self.colonne))
        else:
            for j in range(self.longueur):
                positions.append((self.ligne, self.colonne+j))
        return positions
    
    def chevauche(self, autre):
        return not set(self.positions).isdisjoint(autre.positions)
    
    def coulé(self, g):
        for tuple in self.positions:
            if g.matrice[(tuple[0])*g.nombre_colonnes+(tuple[1])] != g.touche:
                return False
        return True