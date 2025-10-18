class Bateau:


    def __init__(self, ligne, colonne, longueur = 1, vertical = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = "⛵"


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
        for (l, c) in self.positions:
            if g.matrice[l*g.nombre_colonnes+c] != g.touche:
                return False
        return True
    
class Porte_avion(Bateau):
    def __init__(self, ligne, colonne, vertical = False):
        super().__init__(ligne=ligne, colonne=colonne, longueur=4, vertical=vertical)
        self.marque = "🚢"

class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical = False):
        super().__init__(ligne=ligne, colonne=colonne, longueur=3, vertical=vertical)
        self.marque = "⛴ "
    
class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical = False):
        super().__init__(ligne=ligne, colonne=colonne, longueur=2, vertical=vertical)
        self.marque = "🚣"

class Sous_marin(Bateau):
    def __init__(self, ligne, colonne, vertical = False):
        super().__init__(ligne=ligne, colonne=colonne, longueur=2, vertical=vertical)
        self.marque = "🐟"
    
        