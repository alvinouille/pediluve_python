import sys
def open_file(text):
    file = open(text)
    string = file.read()
    return string

def create_dict(liste):
    dict = {}
    for i in range(len(liste)):
        dict[liste[i][0]] = liste[i][1]
    return dict 


new = open_file("petite.txt").split("\n")
liste = []
for a in new:
    liste.append(a.split(":"))

dict_word = create_dict(liste)