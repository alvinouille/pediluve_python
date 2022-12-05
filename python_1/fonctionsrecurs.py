# FONCTIONS RECURSIVES
def multiple(n, limit):
    if n > limit:
        return
    print(f"n = {n}")
    multiple(n*n, limit)

multiple(2, 1000)

#la ce sera bon car return avant recursion : repart du tt debut
#sinon on reste ds la fonction 1x recursion finie : resultat none
def demanderchoix (min, max):
    rep = input (f"Faites un choix entre {min} et {max} :")
    try:
        goodrep = int(rep)
        if not min <= goodrep <= max:
            print("ERREUR : le chiffre n est pas ds le bon intervalle")
            return demanderchoix(min, max)
        else:
            return goodrep
    except:
        print("FAIL ! rentrez un chiffre svp")
        return demanderchoix(min, max)

choix = demanderchoix(0, 10)
print("choix de l utilisateur : ", choix)

#CALLBACKS : passer en parametre dune fct1 une fct2 a utiliser ds la fct1
#+ possibilite stocker ds variable le nom dune fonction = change son nom

def table(n, operateur_str, operation):
    for i in range (0, 10):
        print(f"{i} {operateur_str} {n} = ", operation(i, n))


def puissance(a, b):
    return pow(a ,b)

table(5, "^", puissance)
print()

# FONCTION LAMBDA -> svt utilisee ds fonction aysnchrone = effectue tache en mm tps
# code continue a etre execute (bloque pas le code)

table(5, "*", lambda a, b : a*b)


#nombre var de param :
#mettre * dvt un param : permet de passer nb var param


def somme(titre, *nombres):
    resultat = 0
    for n in nombres:
        resultat += n
    return resultat

print(somme("sommes des nb :", 5, 2, 4))

'''#** : cle = valeur (pr chaque valeur on donne une cle)
def somme(titre, **nombres):
    resultat = 0
    for n in nombres.values():
        resultat += n
    return resultat

print(somme("sommes des nb :", maths=5, anglais=2, geo=4))
#cest grace a .values() auon recupere les valeurs associees aux cles'''