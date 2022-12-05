import random
#la maniere de placer k a chaque fois
player = {1 : "X", 2 : "O"}

def last_choice(p, grille):
    other = 3 - p
    #verifie si 2 meme signe de moi dans grille
    if checking(p, grille, 2)!= None:
        return checking(p, grille, 2)
    #verifie si 2 signe de l'autre joueur dans la grille
    elif checking(other, grille, 2) != None:
        return checking(other, grille, 2)
    else:
        return None

def logical_choice(p, grille):
    other = 3 - p
    if checking(p, grille, 1) != None:
        return checking(p, grille, 1)
    else:
        return None


def total_checker(a, b, c, sign, nonsign, nb):
    if nb == 2:
        if a == sign and a == b and c != nonsign:
            return c
        elif a == sign and a == c and b != nonsign:
            return b
        elif b == sign and b == c and a != nonsign:
            return a
        else:
            return None
    if nb == 1:
        if a == sign and b != nonsign and c != nonsign:
            choice = random.choice("bc")
            if choice == "b":
                return b
            else:
                return c
        if b == sign and c != nonsign and a != nonsign:
            choice = random.choice("ac")
            if choice == "a":
                return a
            else:
                return c
        if c == sign and a != nonsign and b != nonsign:
            choice = random.choice("ab")
            if choice == "a":
                return a
            else:
                return b
        else:
            return None

    
def line_checker(pl, grille, a):
    i = 0
    while i < 9:
        if i == 0 or i == 3 or i == 6:
            if total_checker(grille[i], grille[i + 1], grille[i + 2], player[pl], player[3 - pl], a) != None:
                return total_checker(grille[i], grille[i + 1], grille[i + 2], player[pl], player[3 - pl], a)
        i += 1
    return None

def col_checker(pl, grille, a):
    i = 0
    while i < 9:
        if i == 0 or i == 1 or i == 2:
            if total_checker(grille[i], grille[i + 3], grille[i + 6], player[pl], player[3 - pl], a) != None:
                return total_checker(grille[i], grille[i + 3], grille[i + 6], player[pl], player[3 - pl], a)
        i += 1
    return None

def diag_checker(pl, grille, a):
    i = 0
    while i < 9:
        if i == 0:
            if total_checker(grille[i], grille[i + 4], grille[i + 8], player[pl], player[3 - pl], a) != None:
                return total_checker(grille[i], grille[i + 4], grille[i + 8], player[pl], player[3 - pl], a)
        elif i == 2:
            if total_checker(grille[i], grille[i + 2], grille[i + 4], player[pl], player[3 - pl], a) != None:
                return total_checker(grille[i], grille[i + 2], grille[i + 4], player[pl], player[3 - pl], a)
        i += 1
    return None

def checking(pl, grille, a):
    #LIGNE:
    if line_checker(pl, grille, a) != None:
        return line_checker(pl, grille, a)
    #COLONNE:
    elif col_checker(pl, grille, a) != None:
        return col_checker(pl, grille, a)
    #DIAG:
    elif diag_checker(pl, grille, a) != None:
        return diag_checker(pl, grille, a)
    else:
        return None
