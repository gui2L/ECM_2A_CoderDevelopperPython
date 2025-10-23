from grille import Grille
from bateau import *

def main():
    print("---- Jeu de la Bataille Navale ⛵ ----\n")
    
    
    while True:
        mode = input("Veuillez saisir le mode de jeu (test ou default) : ")
        if (mode == "test" or mode == "default"):
            break
        else:
            print("❌ Saisie invalide ! Veuillez entrer correctement le mode de jeu")

    print("\n --> la partie commence ! \n")

    g = Grille(8, 10)
    types_bateau = [Porte_avion, Croiseur, Torpilleur, Sous_marin]
    for type in types_bateau:
        g.placer_aleatoirement(type)
    
    info_du_tir = {"id": 0, "message" : ""}
    g.afficher(mode) 
    while info_du_tir["id"] != -1:
        while True:
            try:
                x, y = map(int, input("Entrez les coordonnées x et y séparées par un espace pour effectuer un tir: ").split())
                break  
            except ValueError:
                print("❌ Saisie invalide ! Veuillez entrer deux nombres séparés par un espace.")
        info_du_tir = g.tirer(x-1, y-1)
        g.afficher(mode)
        print(f">> Tir n°{g.nb_coup} éxécuté en ({x}, {y}) 🎯")
        print(info_du_tir["message"])

    print("\n --> la partie est terminée ! \n")
    print(f"Nombre total de coups (tirs) = {g.nb_coup}")
    print(f"score = {round(11*10/g.nb_coup, 2)}")

    return 0



if __name__ == "__main__":
    main()