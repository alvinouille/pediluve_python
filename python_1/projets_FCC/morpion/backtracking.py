from validity_check import *
from placement_check import *
import random

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

def put_random_nb_left(grille):
    nb_left = ""
    for nb in grille:
        if nb.isdigit():
            nb_left = nb_left + nb
    return random.choice(nb_left)

def line_valid(grille):
    i = 0
    while i < 9:
        if (i == 0 or i == 3 or i == 6) and (grille[i] == grille[i + 1] == grille[i + 2]):
            return grille[i]
        i += 1
    return None

def column_valid(grille):
    i = 0
    while i < 9:
        if (i == 0 or i == 1 or i == 2) and (grille[i] == grille[i + 3] == grille[i + 6]):
            return grille[i]
        i += 1
    return None

def diag_valid(grille):
    i = 0
    while i < 9:
        if i == 0 and (grille[i] == grille[i + 4] == grille[i + 8]):
            return grille[i]
        elif i == 2 and (grille[i] == grille[i + 2] == grille[i + 4]):
            return grille[i]
        i += 1
    return None

def grille_valid_or_draw(grille, p):
    # Si player gagnant, return True, si grille gagnante mais pas par player : mauvais, return False
    if line_valid(grille) != None:
        if player[p] == line_valid(grille):   
            return True
        else:
            return False
    elif column_valid(grille) != None:
        if player[p] == column_valid(grille):
            return True
        else:
            return False
    elif diag_valid(grille) != None:
        if player[p] == diag_valid(grille):
            return True
        else:
            return False
    # Si aucune suite valide mais grille remplie : egalite
    elif full_check(grille):
        return True
    # Sinon (si grille pas remplie et aucune suite valide) 
    else:
        return False

def is_valid(grille, p, pdep):
    
    print_grille(grille)
    print()
    choice = ""
    player_origin = pdep

    # si on sort du tableau(10eme case) # A FAIRE : grille validity selon joueur: / grille validity = gagnante ou EGALITE = grille non perdante
    if grille_valid_or_draw(grille, pdep):
        return True
    
                #    BACKTRACKING
    k = player[p]
 
    while grille_valid_or_draw(grille, 3 - pdep) == 0:    # tant qu'on a pas de grille gagnante, on met pas le signe, si on en a une, on l'assigne et on passe au coup suivant
        #i = pos + 1
        # si il reste 1 coup gagnant ou perdant alors on le fait et on met a jour : jeu termine perdu ou gagnant : on va inscrire ou pas le chiffre, si perdant : on inscrit pas et on teste en mettant autre part
        if last_choice(p, grille) != None:
            choice = str(last_choice(p, grille))
        # s'il reste encore des coups a jouer inconnus alors on choisi coup logique, si pas de logique coups au hasard
        else:
            choice = str(logical_choice(p, grille))
        grille = grille.replace(choice, k)
        # coup joue, on passe au joueur suivant 
        if is_valid(grille, 3 - p, pdep):
            return True
        # sinon on efface la case et on revient au debut


# RESTE A FAIRE : logique des coups + implementer dans fonction qui ecrira le coup que si il a trouve une grille gagnante ou egalite avec ce coup de ce joueur
    grille = grille.replace(k, choice)
    return False
    # il manque le backtrack lorsque c pas le gagnant qu'on veut


#jouer coup random si jeu pas commence, sinon :
#choice = put_random_nb_left(grille)
#lancer algo backtrack pour determiner reste jeu
grille = "OXO4OX789"
print_grille(grille)
print("-----------------")

if is_valid(grille, 1, 1):
    print("grille remplie")
else:
    print("non")


#print_grille(grille)