class etre_vivant:
    ESPECE = "etre vivant"
    def afficher_espece(self):
        print("Je suis un " + self.ESPECE)

class chat(etre_vivant):
    ESPECE = "mammifere"
    
class personne(etre_vivant):
    ESPECE = "humain"
    def __init__(self, nom_p : str , age_p : int):
        self.nom = nom_p
        self.age = age_p
    
    def afficher_info_personne(self):
        print(f"Bonjour je m'appelle {self.nom}, j'ai {self.age} ans.")
   
class etudiant(personne):
    def __init__(self, nom_p : str , age_p : int, etude_p : str):
        # self.nom = nom_p
        # self.age = age_p
        super().__init__(nom_p, age_p)
        self.etude = etude_p
    def afficher_info_personne(self):
        super().afficher_info_personne()
        print("Je suis etudiant en : " + self.etude)
    


chat1 = chat()   #la classe chat est la classe enfant de la classe etre vivant
chat1.afficher_espece()
etre_vivant1 = etre_vivant()
etudiant1 = etudiant("Alvina", 25, "ecole 42")
etudiant1.afficher_info_personne()
etudiant1.afficher_espece()