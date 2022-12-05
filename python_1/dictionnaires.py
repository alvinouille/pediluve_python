# LES DICTIONNAIRES
# dictionne = {"cle" : "valeur", "cle" : "valeur"}

personne = {"nom":"Alvina", "age":25, "taille":1.62}
print(personne["nom"]) #donne valeur attribuee a cle nom
print(personne["age"]) #donne valeur attribuee a cle age

personne["nom"] = "Claire" #remplace valeur Alvina par Claire
personne["poste"] = "developpeur" #rajoute une cle + valeur

achat = ("beurre", "chocolat", "cacahuete")
personne["achats"] = achat

#pour imprimer contenu du dictionnaire:
for i in personne:
    print(f"cle : {i}, valeur : {personne[i]}")
