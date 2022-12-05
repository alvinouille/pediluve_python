# EXO : LISTER NOMS DE PERSONNES

liste_nom = []
nom = ""
nom = input("rentrez votre nom : ")
liste_nom.append(nom)
while not nom == "":
    nom = input("rentrez votre nom : ")
    liste_nom.append(nom)
print(*liste_nom[:])
#si on veut la liste triee ordre ascii :
liste_nom.sort()
for nom in liste_nom:
    print(" " + nom)

#OU

'''while True:
     nom = input("rentrez votre nom : ")
     if nom == "":
        break
    liste_nom.append(nom) '''
