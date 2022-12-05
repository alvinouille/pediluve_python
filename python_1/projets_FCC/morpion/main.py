import time
from validity_check import *

def print_grille(grille):
    a = 0
    b = 3
    while b < 10:
        print("|", end = "")
        for carreau in grille[a:b]:
            print(carreau, end ="|")
        print()
        a += 3
        b += 3

def change_number(grille, number, player):
    if player == 1:
        grille = grille.replace(number, "X")
    else:
        grille = grille.replace(number, "O")
    return grille

def full_check(grille):
    return all([True if nb == "X" or nb == "O" else False for nb in grille])

grille = "123456789"
print_grille(grille)

j1 = input("Nom du premier joueur : ")
j2 = input("Nom du deuxieme joueur : ")
print(f"OK {j1} et {j2}, c'est parti !")
time.sleep(1)
pl = 1

while grille_validity(grille) == 0 and full_check(grille) == 0:
    if pl == 1:
        res = input(f"{j1} : ")
        if number_validity(res, grille):
            grille = change_number(grille, res, pl)
            print_grille(grille)
            time.sleep(1)
            pl = 2
            #print(f"grille validite : {grille_validity(grille)} et remplissage: {full_check(grille)}")
        else:
            print("Mauvaise reponse, veuillez donner un chiffre qui est toujours dans la grille")
    else:
        res = input(f"{j2} : ")
        if number_validity(res, grille):
            grille = change_number(grille, res, pl)
            print_grille(grille)
            time.sleep(1)
            pl = 1
        else:
            print("Mauvaise reponse, veuillez donner un chiffre qui est toujours dans la grille")

if grille_validity(grille):
    if pl == 2:
        print(f"BRAVO {j1}, TU AS GAGNE !")
    else:
        print(f"BRAVO {j2}, TU AS GAGNE !")
else:
    print("Egalite !")