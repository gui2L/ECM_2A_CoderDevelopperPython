from bateau import Bateau

class Grille:
    vide = "〰️" 
    icon_bat = "⛵"
    touche = "💥"


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

    def tirer(self, x:int, y:int, touche=touche):
        if (x < 0 or x >= self.nombre_lignes or y < 0 or y >= self.nombre_colonnes):
            print("coordonnées invalides")
            return -1
        else:
            if (self.matrice[(x)*self.nombre_colonnes+(y)] != touche):
                self.matrice[(x)*self.nombre_colonnes+(y)] = touche
                print(f"case ({x}, {y}) touchée")
            else:
                print(f"case ({x}, {y}) déjà touchée")
        print()
        
        return (x)*self.nombre_colonnes+(y)
                
    def ajoute(self, bateau):
        pos = []
        for i in range(bateau.longueur):
            x = bateau.positions[i][0]
            y = bateau.positions[i][1]
            if (x < 0 or x >= self.nombre_lignes or y < 0 or y >= self.nombre_colonnes):
                break
            pos.append((x, y))

        if (len(pos) == bateau.longueur):
            for i in range(bateau.longueur):
                x = pos[i][0]
                y = pos[i][1]
                self.matrice[(x)*self.nombre_colonnes+(y)] = bateau.marque
            return True
        else:
            print(f"le bateau de coords : {bateau.positions} ne rentre pas dans la grille\n")
            return False
        




    
        
        

