''' collections = liste, tableau, tuple
tuple() : immutable -> non modifiable
liste[] : mutable -> modifiable : rajouter/supprimer des elements
ou les modifier'''

# LES TUPLES

'''personnes = ("melanie", "jean", "martin")
print(personnes[-1])
print(len(personnes))
for i in range(0, len(personnes)):
    print(personnes[i])

#for i in range (index0, index non compris)
for i in personnes:
    print(i)
    print(len(i))
    print(i[-1])'''

# LES LISTES

'''personnes = ["melanie", "jean", "martin"]
nouvelle_personne = "David"
personnes.append(nouvelle_personne)
del personnes[1]
print(personnes)
for i in personnes:
    print(i)

def modif_valeur(a):
    a[2] = 10

test = [1, 2, 3, 4]
print(test)
modif_valeur(test)
print(test)'''

# FONCTIONS ET TUPLES

'''def obtenir_info():
    return "Melanie", 37, 1.75

def afficher_info(nom, age, taille):
    print(f"{nom} a {age} ans et fait {taille}m !")

infos = obtenir_info()
afficher_info(*infos) #on ouvre tuple avec *tuple, pour 
#les passer dans les params, sinon le tuple rentrerait en entier dans le param1
#ex :
print(infos)
print(*infos) # = unpack le tuple'''

# LES SLICES

personnes = ("Melanie", "Jean", "Martin", "Pierre")
 
# [start:stop(non inclu):step]
for i in personnes[0:2]:
    print(i)
for i in personnes[:]: #->tlm
    print(i)
for i in personnes[::2]: #-> tous les 2
    print(i)
for i in personnes[::-1]: #-> tout dans le sens inverse
    print(i)
print()
nom = "Alvina"
for i in nom[::-1]:
    print(i, end="")
print() # OU, PLUS SIMPLE:
print(nom[::-1])