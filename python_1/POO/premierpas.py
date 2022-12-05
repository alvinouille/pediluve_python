def afficher_info_personne(nom, age):
    print(f"La personne s'appelle {nom} et a {age} ans.")

def demander_nom_personne():
    nom = input("Quel est votre nom ?")
    return nom

nom1 = "Jean"
age1 = 30

nom2 = "Martin"
age2 = 45

afficher_info_personne(nom1, age1)
afficher_info_personne(nom2, age2)

nom3 = demander_nom_personne()
age3 = 18
afficher_info_personne(nom3, age3)