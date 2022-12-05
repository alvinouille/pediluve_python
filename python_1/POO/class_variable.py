class personne:
    ESPECE = "Humain"     # variable de classe:depend pas d'instance
    def __init__(self, nom_p : str = "", age_p : int = 0):
        if nom_p != "":
            self.nom = nom_p
        else:
            self.nom = self.demander_nom()    # creation variable d'instance
        self.age = age_p
    
    def afficher_info_personne(self):
        if self.age != 0:
            print(f"Bonjour je m'appelle {self.nom}, j'ai {self.age} ans.")
            if self.estMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
        else:
            print(f"Bonjour je m'appelle {self.nom}")
         
    def estMajeur(self):
        return self.age >= 18

    def demander_nom(self):
        return input("Quel est votre nom ?")
    
    def afficher_espece(self):
        print("Je suis " + personne.ESPECE)    #appel de v de c
       
#       UTILISATION

liste_personnes =[personne("Paul", 15), personne("Dom", 45), personne("Zoe", 18)]
i = 0
liste_personnes.append(personne("Sophie", 24))
personne.ESPECE = "mutant"
#liste_personnes[0].espece = "mutant"    #on altere variable de classe
while i < len(liste_personnes):
    liste_personnes[i].afficher_info_personne()
    liste_personnes[i].afficher_espece()      #methode de classe
    i += 1

'''Personne
        -> Personne.espece
    personne1
        -> personne1.espece (copie de la variable de c;asse pur en faire 
                            variable d'instance)
    personne2
        -> personne2(/self).espece
    personne3
        -> personne3.espece     '''
