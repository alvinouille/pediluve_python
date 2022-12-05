'''def create_dict(string):
    dictionnary = {}
    for i in range(len(string)):
        print(i)
        dictionnary[i] = string[i].upper()
    print(dictionnary)

create_dict("Yopla")

def hiden_word(word):
    new = ""
    for i in range(len(word)):
        new += "-"
        new += " "
    print(new)

def print_word(word):
    for i in range(len(word)):
        print(f"{word[i]} ", end = "")
hiden_word("Salut")
print_word("salut")'''

'''liste = []
for i in range(2):
    user_letter = input("Guess a letter : ")
    liste.append(user_letter.upper())
print(*liste)'''

'''from words import list_words
import random
word = random.choice(list_words)
print(word)'''

'''answer = "- - - - -"
print(answer)
user_letter = "a"
answer = answer[:2] + "a" + answer[2+1:]
print(answer)'''

'''def check_word(new):
    if "-" in new:
        print(True)
    else:
        print(False)

check_word("----")'''

'''chaine = "ballon"
#nb = chaine.count("l")
#print(nb)
def find_nth_occ(chaine, char, occ):
    first = chaine.find(char)
    i = 1
    while i != occ:
        first = chaine.find(char, first + 1)
        i += 1
    return first

first_i = chaine.index("l")
second = find_nth_occ(chaine, "l", 2)
print(first_i)
print(second)'''