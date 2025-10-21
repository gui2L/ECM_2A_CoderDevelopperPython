from grille import Grille
from bateau import *

def main():
    g = Grille(8, 10)
    types_bateau = [Porte_avion, Croiseur, Torpilleur, Sous_marin]
    for type in types_bateau:
        g.placer_aleatoirement(type)
    
    info_du_tir = {"id": 0, "message" : ""}
    g.afficher() 
    while info_du_tir["id"] != -1:
        while True:
            try:
                x, y = map(int, input("Entrez les coordonnées x et y séparées par un espace : ").split())
                break  
            except ValueError:
                print("❌ Saisie invalide ! Veuillez entrer deux nombres séparés par un espace.")
        info_du_tir = g.tirer(x-1, y-1)
        if (info_du_tir["id"] != -1) :
            g.afficher()
            print(info_du_tir["message"])
            print(f"🎯 Nombre de tirs éxécutés : {g.nb_coup}")

    print(info_du_tir["message"])
    return 0



if __name__ == "__main__":
    main()