
def open_file(text):
    file = open(text)
    string = file.read()
    return string

def replace_char_fr(a):
    a = a.replace("é", "e")
    a = a.replace("à", "a")
    a = a.replace("ç", "c")
    a = a.replace("è", "e")
    a = a.replace("ô", "o")
    a = a.replace("â", "a")
    a = a.replace("ê", "e")
    a = a.replace("î", "i")
    a = a.replace("œ", "oe")
    return a

def remove_wrong_w(liste):
    [liste.remove(mot) if "'" in mot else mot for mot in liste]
    [liste.remove(mot) if "-" in mot else mot for mot in liste]
    return liste

liste = (replace_char_fr(open_file("list.txt"))).split(", ")
liste = remove_wrong_w(liste)


