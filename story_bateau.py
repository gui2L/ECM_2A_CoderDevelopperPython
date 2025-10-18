from bateau import Bateau

#   Nom : "chevauchement"
#   Utilisateur : un joueur
#   Story : Positionner des bateaux sans chevauchement

#   Actions :

#1.créer un bateau b1
b1 = Bateau(2, 3, 4)

#2.créer un bateau b2
b2 = Bateau(1, 4, 2, True)

#3.créer un bateau b3
b3 = Bateau(3, 5, 4)

print(f"b1 : {b1.positions}")
print(f"b2 : {b2.positions}")
print(f"b3 : {b3.positions}\n")

#3.Vérifier si les deux bateaux se chevauchent
if b1.chevauche(b2):
    print("b1 chevauche b2")
else:
    print("b1 ne chevauche pas b2")

if b1.chevauche(b3):
    print("b1 chevauche b3")
else:
    print("b1 ne chevauche pas b3")

if b2.chevauche(b3):
    print("b2 chevauche b3")
else:
    print("b2 ne chevauche pas b3")