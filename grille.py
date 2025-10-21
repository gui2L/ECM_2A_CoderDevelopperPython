from bateau import Bateau
import random

class Grille:
    vide = "〰️" 
    icon_bat = "⛵"
    touche = "💥"
    types = {"⛵" : "default", "🚢" : "Porte-avion", "⛴ " : "Croiseur", "🚣" : "Torpilleur", "🐟" : "Sous_marin"}

    def __init__(self, nombre_lignes=4, nombre_colonnes=4):
        self.matrice = [Grille.vide for _ in range(nombre_colonnes*nombre_lignes)]
        self.nombre_colonnes = nombre_colonnes
        self.nombre_lignes = nombre_lignes
        self.bateaux = {}
        self.nb_bateau_coule = 0
        self.nb_coup = 0

    def __str__(self):
        lignes = []
        for i in range(self.nombre_lignes):
            ligne = ""
            for j in range(self.nombre_colonnes):
                ligne += self.matrice[i*self.nombre_colonnes+j]
            lignes.append(ligne)
        return "\n".join(lignes)


    def afficher(self):
        col = "  "
        for i in range(self.nombre_colonnes):
            col += f"{i+1} "
        print(col)
        for i in range(self.nombre_lignes):
            ligne = f"{i+1}"
            for j in range(self.nombre_colonnes):
                if self.matrice[i*self.nombre_colonnes+j] == Grille.touche:
                    ligne += self.matrice[i*self.nombre_colonnes+j]
                else:
                    ligne += Grille.vide
            print(ligne)
        print()

    def tirer(self, x:int, y:int, touche=touche):
        if (x < 0 or x >= self.nombre_lignes or y < 0 or y >= self.nombre_colonnes):
            print("coordonnées de tir invalides")
            return 0
        else:
            self.nb_coup += 1
            case = self.matrice[(x)*self.nombre_colonnes+(y)]
            if (case == Grille.vide):
                print(f"rien touché en ({x+1}, {y+1})")
            elif (case == touche):
                print(f"bateau en ({x+1}, {y+1}) déjà touché")
            else:
                marque = case
                self.matrice[x*self.nombre_colonnes+y] = touche
                print(f"bateau touché en ({x+1}, {y+1})")
                if(self.bateaux[marque].coulé(self)):
                    self.nb_bateau_coule += 1
                    if (self.nb_bateau_coule == len(self.bateaux.keys())):
                        print(f"{Grille.types[marque]} {marque} coulé !") 
                        print("TOUS LES BATEAUX ONT ETE DETRUITS --> PARTIE GAGNEE !")
                        print(f"score = {self.nb_coup} (tirs)")
                        return -1
                    else:
                        print(f"{Grille.types[marque]} {marque} coulé ! encore {len(self.bateaux.keys())-self.nb_bateau_coule} à couler")     
        print()
        return 1
                
    def ajoute(self, bateau):
        if self.peut_placer(bateau):
            for (l, c) in bateau.positions:
                self.matrice[l*self.nombre_colonnes+c] = bateau.marque
            self.bateaux[bateau.marque] = bateau
            return True
        else:
            print(f"le bateau de coords : {bateau.positions} ne rentre pas dans la grille\n")
            return False

    def peut_placer(self, bateau):
        for (l, c) in bateau.positions:
            if l < 0 or c < 0 or l >= self.nombre_lignes or c >= self.nombre_colonnes:
                return False
            
        for b in self.bateaux.values():
            if bateau.chevauche(b):
                return False

        return True

    def placer_aleatoirement(self, type_bateau):
        pos_possibles = []
        for ligne in range(self.nombre_lignes):
            for colonne in range(self.nombre_colonnes):
                for vertical in (True, False):
                    b = type_bateau(ligne, colonne, vertical)
                    if self.peut_placer(b):
                        pos_possibles.append(b)

        if not pos_possibles:
            raise RuntimeError("Aucun placement possible pour ce bateau !")

        choisi = random.choice(pos_possibles)
        self.ajoute(choisi)
        return choisi



    
        
        

