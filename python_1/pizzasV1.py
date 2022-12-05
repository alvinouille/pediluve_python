def pizza_existe(liste, new):
    for i in range(len(liste)):
        if new == liste[i] or new.lower() == liste[i]:
            return True
    return False

def tri_perso(e):
    #return e : signifie tri par ordre ascii par defaut
    return len(e) #tri par longueur mot de la liste

def afficher(liste, nbpizza, nb=0):
        if nb != 0:
            print(f"--- LISTE DES PIZZAS ({nbpizza}) ---")
        #liste.sort(reverse = True) #tri /ordre ascii inverse
        #liste.sort(key = tri_perso) #on peut lui passer une fct
            liste.sort(reverse = 1, key = tri_perso) #tri /ordre nb lettre inverse
            for i in liste[0:nb]:
                print(i)
            print(f"\nPremiere pizza: {liste[0]}")
            print(f"Derniere pizza: {liste[-1]}")
        else:
            return

def affichepizza(liste):
    nb = 0
    if len(liste) == 0:
        print("AUCUNE PIZZA")
        return
    new = input("Pizza a ajouter : ")
    if new != "" and pizza_existe(liste, new) == 0:
        liste.append(new)
        afficher(liste, len(liste), 3)
    else:
        return affichepizza(liste) 

collection = ["4 fromages", "mortone", "galanei"]
vide = []
affichepizza(collection)

