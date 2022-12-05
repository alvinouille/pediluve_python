# Personne (entite -> class)
#       Donnees : nom, age
#       Actions : (methodes)
#           - sePresenter() 
#           - demanderNom() / input

#       DEFINITION

class personne:
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
       
#       UTILISATION

#personne1 = personne("Paul", 15)
#personne2 = personne("Dom", 45)
#personne1.nom = "Georges"      #altere valeur personn1
#personne3 = personne()
#personne4 = personne(age=20)    #pour indiquer le nom du param qd ordre param non respecte
#personne1.afficher_info_personne()
#personne2.afficher_info_personne()  #methode d'instance
#personne3.afficher_info_personne()
#personne4.afficher_info_personne()
#personne.autre_fct()         # methode de classe : plus acces 
                            #au self, methode pour ts les objets
#print(f"est majeur :{personne1.estMajeur()}")
#print(f"est majeur :{personne2.estMajeur()}")

liste_personnes =[personne("Paul", 15), personne("Dom", 45), personne()]
i = 0
liste_personnes.append(personne("Sophie", 24))
while i < len(liste_personnes):
    liste_personnes[i].afficher_info_personne()
    i += 1

#OU

