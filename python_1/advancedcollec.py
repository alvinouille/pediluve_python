# LES COLLECTIONS ; LISTE / TUPLES
# Append / extend / += / insert

noms = ["Jean", "Martin"]
noms.append("Toto")
print(*noms)
noms.extend(["Marvella", "Beatrice"]) # = 'noms += autresnoms
print(*noms)
def ft_extend(liste):
    for i in liste:
        noms.append(i)
ft_extend(["Marine", "Roberta"])
print(*noms)

noms.insert(0, "Darling") #insert a l'index 0
noms = ["Fukushima"] + noms  # concatene liste
print(*noms)

# LES SLICES : selectionne certains elem ds liste

slice_nom = noms[:] #cree nvelle liste en copiant liste
print(slice_nom)

# Tris : Sort / sorted

noms.sort()  #on modifie la liste direct a l'interieure
new = sorted(noms)  #sort la copie de la liste triee
noms.sort(key = lambda nom:len(nom)) #lambda : passer fct direct
                                    #nom : prend en param, len(nom) : trier en fct de ca

#operations sur les elements : min, max, in, sum
ages = [21, 56, 3, 256]
print(min(ages))    #donne min de liste selon ascii
print(max(ages))
print(min(noms))

if "Beatrice" in noms:   #in : pr savoir si present liste ou pas
    print("oui")
else:
    print("non")

print(sum(ages)) #calcul somme int

#le SWAP
nom = ["Alice", "Baptiste", "Celine", "Marguerite"]
nom[0], nom[2] = nom[2], nom[0] #fait ca direct donc ca marche
print(*nom)

#fct JOIN et SPLIT (string et collections) : permet parsing
#join
collection = ["Julie", "Marie"]
nouvelle = "caracsepara".join(collection)
print(nouvelle)  # -> on obtient string
#split
collec = "Paul, Marc, Emilie"
a_split = collec.split(", ")
print(a_split)   # -> on obtient liste

#index, find et count
#trouver un element ds une liste
print(nom.index("Alice", indexdebut, indexfin)) 
#trouver nb occurrence elem ds une liste
nb_occ = noms.count("Alice")
#find
string.find("Martin") # -> donne lindex du mot qui ets trouve dans la tring
#si pas trouve : -1


