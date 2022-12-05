def line_validity(grille):
    i = 0
    while i < 9:
        if (i == 0 or i == 3 or i == 6) and (grille[i] == grille[i + 1] == grille[i + 2]):
            return True
        i += 1
    return False

def column_validity(grille):
    i = 0
    while i < 9:
        if (i == 0 or i == 1 or i == 2) and (grille[i] == grille[i + 3] == grille[i + 6]):
            return True
        i += 1
    return False

def diag_validity(grille):
    i = 0
    while i < 9:
        if i == 0 and (grille[i] == grille[i + 4] == grille[i + 8]):
            return True
        elif i == 2 and (grille[i] == grille[i + 2] == grille[i + 4]):
            return True
        i += 1
    return False

def grille_validity(grille):
    if (line_validity(grille) or column_validity(grille) or diag_validity(grille)):
        return True
    else:
        return False

def is_available(number, grille):
    for i in grille:
        if number in grille:
            return True
    return False

def is_valid(number):
    isnb = number.isdigit()
    islonely = len(number)
    if isnb and islonely == 1:
        return True
    else:
        return False
    

def number_validity(number, grille):
    if is_available(number, grille) and is_valid(number):
        return True
    else:
        return False
