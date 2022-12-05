from words import liste
from drawings import lives_visual_dict
import random

def is_in_word(word, letter):
    try:
        index = word.index(letter)
        return index
    except:
        return None
            

def hiden_word(word):
    new = ""
    for i in range(len(word)):
        new += "-"
    return new

def print_word(word):
    for i in range(len(word)):
        print(f"{word[i]} ", end = "")

def check_word(new):
    if "-" in new:
        return True
    else:
        return False

def find_nth_occ(chaine, char, occ):
    firstocc = chaine.find(char)
    i = 1
    while i != occ:
        otherocc = chaine.find(char, firstocc + 1)
        i += 1
    return otherocc

#option : rajouter : essayer le mot en entier pour gagner
word = random.choice(liste)
print(word)
lives = 7
list_letter = []
answer = hiden_word(word)
first_i = 0

while (lives > 0) and (check_word(answer) != 0):
    user_letter = input("Devinez une lettre : ")
    list_letter.append(user_letter.upper())
    first_i = is_in_word(word, user_letter)
    #print(index)
    #print(lives)
    if not first_i == None:
        print(f"Yay! Votre lettre {user_letter} est dans le mot.")
        totale_occ = word.count(user_letter)
        answer = answer[:first_i] + user_letter.upper() + answer[first_i +1:]
        if totale_occ > 1:
            nb_occ = 2
            while totale_occ >= nb_occ:
                occ = find_nth_occ(word, user_letter, nb_occ)
                answer = answer[:occ] + user_letter.upper() + answer[occ +1:]
                nb_occ += 1
    else:
        lives -= 1
        print(f"Votre lettre {user_letter} n'est pas dans le mot.")
        print(lives_visual_dict[lives])
        print(f"Il vous reste {lives} vies et vous avez donne ces lettres: ", end = "")
        print(*list_letter)
    print("Mot : ", end = "")
    print_word(answer)
    print()
if lives == 0:
    print(f"Sorry, vous etes morts. Le mot etait : {word.upper()}")
else:
    print(f"VOUS AVEZ GAGNE, BRAVO!")
