noms = ["Jean", "Christophe", "Maria"]

longueur = []
'''for nom in noms:
    longueur.append(len(nom))'''
longueur = [len(nom) for nom in noms] #nvelle liste longueur nom pour chq nom dans noms
#tjrs commencer : nom for nom in nom
print(longueur)
# + avec des criteres :
longueur = [len(nom) for nom in noms if "e" in nom]
print(longueur)

longueur = [len(nom) if len(nom) < 10 else 0 for nom in noms]

a = [i for i in range(5) if i%2 == 0]
print(a)

b = [(j, True if j%2 == 0 else False) for j in range(5)]
print(b)

#any et all
a = [True, False, True]
print(any(a)) # retourne True qd >=1 elem est True
print(all(a)) # retourne True qd tt les elem sont True

noms = ["Marie", "Zoe", "Zaid", "Carmen"]
found = False
for nom in noms:
    if "z" in nom.lower():
        found = True
        break
if found:
    print("Trouve")
else:
    print("Non trouve")

noms_avec_un_z_existe = any([True if "z" in nom.lower() else False for nom in noms])
if noms_avec_un_z_existe:
    print("Trouve!")
else:
    print("Nop!")

#tester si une chaine contient des chiffres

prenom = "al25vina"
a = any([True if prenom.isdigit() == True else False for prenom in prenom])
if a:
    print("Contient des chiffres")
else:
    print("Ne contient pas de chiffre")

#ZIP => fait correspondre 2 listes en creant un tuple avec ces listes : mais a recast en list ou * avant

pizza_nom = ("4 fromages", "Calzone", "Hawai")
pizza_prix = (10.5, 11, 8)
nom_et_prix = list(zip(pizza_nom, pizza_prix))
print(nom_et_prix)
#recuperer les 2 elem du tuple :
for (n, p) in nom_et_prix:   # ne pas oublier les parenthese ni de recast
    print(f"{n} : {p} euros")

unzipped = list(zip(*nom_et_prix))
print(unzipped)   #pour faire linverse 

#LE SET

autreliste = ["Marie", "Jean", "Paul", "Marie"]
set_liste = set(autreliste)   #cree dictionnaire avec cle, sans notion d'ordre (pas dindex!!! mais on peut boucler) sans doublon car une seule cle
print(set_liste)
#mais on peut la stocker dans une liste et la on pourra reindexer du couo
liste_sans_doublon = list(set_liste)
print(liste_sans_doublon[0])
#on peut creer direct set :
setlol = {"Marie", "Germaine", "Marie"} #en mettant direct cle sans valeur
print(setlol)