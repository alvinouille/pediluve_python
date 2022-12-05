# en mode LISTE
personnes = [
    ("Melanie", 25, 1.65),
    ("Paul", 56, 1.75),
    ("Samy", 18, 1.60),
    ("Lola", 30, 1.62)
]

def obtenir_information(nom, liste):
    for i in range(len(liste)):
        if liste[i][0] == nom:
            return liste[i]
    return None

infos1 = obtenir_information("Lola", personnes)
print(infos1)

# en mode DICTIONNAIRE : utile si bcp de donnees : + rapide (acces direct par cle)

personnes_dict = {
    "Melanie": (25, 1.65),
    "Paul": (56, 1.75),
    "Samy": (18, 1.60),
    "Lola": (30, 1.62)
}

infos2 = personnes_dict["Paul"]
print(infos2)

infos2 = personnes_dict.get("Lali") #si cle nexiste pas ca renvoit None
if not infos2:    # = if infos2 == None
    print("La clef n'existe pas")
else:
    print(infos2)