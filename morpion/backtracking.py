from validity_check import *
from placement_check import *

player = {1 : "X", 2 : "O"}

def full_check(grille):
    return all([True if nb == "X" or nb == "O" else False for nb in grille])

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

def is_valid(grille, pos, p):
    
    print_grille(grille)
    print()

    if pos > 8:
        pos = 0
    
    i = pos + 1
    # si on sort du tableau(10eme case) # A FAIRE : grille validity selon joueur 
    if grille_validity(grille):
        return True
    
    if full_check(grille):

        return False

    # si la case n'est pas vide, on passe a la suivante(appel recursif)
    if grille[pos] == "X" or grille[pos] == "O":
        return is_valid(grille, pos+1, p)
    
                #    BACKTRACKING
    a = 0
    k = player[p]
 
    while full_check(grille) == 0:    # faux : A CHANGER, plus tard : tant qu'on a pas de grille gagnante, on met pas le chiffre, si on en a une, on l'assigne et on passe au coup suivant
        i = pos + 1
        # si il reste 1 coup gagnant ou perdant alors on le fait et on met a jour : jeu termine perdu ou gagnant
        if place_k(p, grille) != None:
            i = place_k(p, grille)
            grille = grille.replace(str(i), k)
        # s'il reste encore des coups a jouer inconnus alors on choisit au hasard un de ces coups : A CHANGER
        else:
            grille = grille.replace(str(i), k)
        # coup joue, on passe au joueur suivant : PB : pas besoin de changer de position si on choisit de maniere random un coup
        if is_valid(grille, pos + 1, 3 - p):
            return True


    return False
    # il manque le backtrack lorsque c pas le gagnant qu'on veut



grille = "XO3OXX78O"
print_grille(grille)
print("-----------------")

if is_valid(grille, 2, 1):
    print("grille remplie")
else:
    print("non")


#print_grille(grille)