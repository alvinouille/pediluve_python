# INTRO

print("yo c'est Alvina")
nom = input("entrez votre nom :")
age = 30
print("le nom " + nom + " est de type : ",type(nom),"\n")
print("vous avez ", str(age), "ans\n")
new_age = input("je me suis trompe, donnez moi votre age :")
try:
    new_age = int(new_age) + 5
#si ca marche on execute ca
except:
    print("ERREUR : vous vez mal rentre votre age\n")
#si ca marche pas ca
#possible de mettre quelles exceptions gerer par ex : except ValueError :
else:
    print("dans 6 ans vous aurez :", str(new_age +1), " ans")
#si ca a fonctionne on fait ca en plus


# ok commentaire
""" commentaire
sur plusieurs
lignes"""

# LES BOUCLES
mdp = ""

while not mdp == "alvina":
    mdp = input("Entrez un mdp : ")
print("mdp correct")

# EXEMPLE VARIABLE GLOBALE = pointeurs
variable = "hello"
def modif_var():
    global variable
    variable = input("rentrez la variable lol : ")

modif_var()
print (variable)

# CONDITIONS

if 12 < age <= 15:
    "you re such a baby"
elif age == 16 or age == 18:
    "its better but still not worth it"
else:
    "ok gotcha"

# BOUCLE FOR

# pour i qui boucle de 0 (inclu) a 4(non inclu)
NB_PERSONNE = 10 #on ne modifie jms une var en maj = constante par convention
for i in range(0, 4):
    print(i)
for i in range (0, NB_PERSONNE):
    print("yo" + str(i))

# PARAM OPTIONNEL

def afficher_info(nom, age, taille=0):
    print(nom, age)
    if taille != 0:
        print(taille)

afficher_info(alvina, 25) #c est ok

# DIFFERENTES SYNTAXES POSSIBLE PRINT

print("vous vous appelez " + nom + ", vous avez " str(age + 1) + "ans")
print(f"vous vous appelez {nom}, vous avez {age} ans")
print("vous vous appelez %s, vous avez %s ans" % (nom, age))
print(""" on met
ce au on
veut""")
print("toto", 20, "ans", "taille", 1.70)