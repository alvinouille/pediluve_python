# Exercice : in insensible a la casse

pren = ["JEAn", "Maria", "Daniel"]

a = any([True if "jean" in lol.lower() else False for lol in pren])
if a:
    print("Yes")
else:
    print("No")


# Exercice : extraire les extensions

fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

def separate_end_file(string):
    liste = string.split(".")
    if len(liste) > 1:
        return liste[-1]
    else:
        return None

def transform_ext_dict(extension):
    dictionnaire = {}
    for i in range(len(extension)):
        dictionnaire[extension[i][0]] = extension[i][1]
    return dictionnaire

def is_in_extension(extension, end):
    liste = []
    found = False
    for i in range(len(extension)):
        chaine = " ".join(extension[i])
        liste.append(chaine)
    found = any([True if end in i.lower() else False for i in liste])
    if found:
        return True
    else:
        return False
'''version plus simple:
def obtenir_def_ext(extension, end):
    for d in extension:
        if d[0].lower == end.lower()
        return d[1]
    return None
'''
# commande: definition = definition_extensions_dict.get(ext.lower())
def print_extension(file, dictionnaire, extensions):
    end = separate_end_file(file)
    if end:
        end = end.lower()
    if end == None:
        print(" (Aucune extension)")
    elif is_in_extension(extensions, end) == True:
        print (f" ({dictionnaire[end]})")
    else:
        print(" (Extension non connue)")




dictionnaire = transform_ext_dict(definition_extensions)
for i in range (len(fichiers)):
    print (fichiers[i], end = "")
    print_extension(fichiers[i], dictionnaire, definition_extensions)


'''
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte)
vacances.jpeg (Image JPEG)
planning (Aucune extension)
data.dat (Extension non connue)
'''

# Exercice : compter le nb total de caractere d'une liste

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

        # Premiere maniere : avec for / len
nb = 0
for i in range(len(noms)):
    nb += len(noms[i])
print(nb)

        # Deuxieme maniere : par completion de liste + sum
longueur_noms = [len(nom) for nom in noms]
print(sum(longueur_noms))

        # Troisieme maniere : avec join / len
print(len("".join(noms)))

