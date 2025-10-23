# Description du répertoire
Projet *Bataille navale* suivant le cours **Coder et développer en python** à *Centrale Méditerranée*

--> Objectif : coder en Python un jeu de bataille navale avec une interface pour un joueur uniquement

Support & règles Version 2.0.0 :
- Grille de taille 8 lignes 10 colonnes 
- **4 types de bateaux à détruire** : {"🚢" : "Porte-avion", "⛴ " : "Croiseur", "🚣" : "Torpilleur", "🐟" : "Sous_marin"}, **placés aléatoirement** sur la grille 
- La partie commence après avoir choisi le **mode de jeu** : **test** (bateaux affichés) ou **default** (bateaux masqués)  
- Convention du développeur :
Les **coordonnées de tir** à saisir (dans le terminal) en tant que joueur **commencent à 1** et non à 0 :

✅ **(1, 1) : case en haut à gauche**, (1, 3), (8, 1), (1, 10), (8, 10)

❌ (0, 0), (0, 1), (1, 0) 
- **La partie se termine une fois tous les bateaux détruits**
- Un **score final** est attribué **en fonction du nombre de tir**

Idées futures implémentations à faire ou en cours de développement :
- UI plus avancée (hors terminal, avec module python)
- génération de grille aléatoire (non rectangulaire, plus de types bateaux)
- mode facile (indication "radar") - mode difficile (bateaux en mouvement à chaque tir ou plus)
- types de tir différents

---

### Version Python utilisée :
Python `3.13.7`

### Récupération du projet sur Github :

### Execution :
- Afin de lancer le jeu, éxécuter, à l'endroit du dossier projet, les commandes suivantes dans le terminal :
```bash
python -m venv venv/
venv\Scripts\activate
venv\Scripts\python -m pip install -r requirements.txt 
python main.py
```
- Une fois le programme éxécuté, il vous sera demandé de selectionner un mode de jeu, la partie commencera alors et vous pourrez effectuer les tirs

---

### License : 

--- 

### Auteur :
Guillaume Surleau - guillaume.surleau@centrale.med.fr