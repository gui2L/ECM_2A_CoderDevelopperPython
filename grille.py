class Grille:
    vide = '~'


    def __init__(self, nombre_lignes=4, nombre_colonnes=4):
        self.matrice = [Grille.vide for _ in range(nombre_colonnes*nombre_lignes)]
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
        print()

    def tirer(self, x:int, y:int):
        if (x <= 0 or x > self.nombre_lignes or y <= 0 or y > self.nombre_colonnes):
            print("coordonnées invalides")
            return -1
        else:
            if (self.matrice[(x-1)*self.nombre_colonnes+(y-1)] != 'x'):
                self.matrice[(x-1)*self.nombre_colonnes+(y-1)] = 'x'
                print(f"case ({x}, {y}) touchée")
            else:
                print(f"case ({x}, {y}) déjà touchée")
        print()
        
        return (x-1)*self.nombre_colonnes+(y-1)
                



    
        
        

