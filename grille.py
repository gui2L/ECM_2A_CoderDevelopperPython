class Grille:
    vide = '~'


    def __init__(self, nombre_lignes=0, nombre_colonnes=0):
        self.matrice = [Grille.vide for i in range(nombre_colonnes*nombre_lignes)]
        self.nombre_colonnes = nombre_colonnes
        self.nombre_lignes = nombre_lignes

    def __str__(self):
        lignes = []
        for i in range(self.nombre_lignes):
            ligne = ""
            for j in range(self.nombre_colonnes):
                ligne += self.matrice[i*self.nombre_colonnes+j]
            lignes.append(ligne)
        return "\n".join(lignes)

    def afficher(self):
        for i in range(self.nombre_lignes):
            ligne = ""
            for j in range(self.nombre_colonnes):
                ligne += self.matrice[i*self.nombre_colonnes+j]
            print(ligne)

    def tirer(self, x:int, y:int):
        self.matrice[x*self.nombre_colonnes+y] = 'x'



    
        
        

