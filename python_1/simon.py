import os
import time
import random

score = 0
seq = ""

for i in range (0, 3):
    chiffre = random.randint(0, 9)
    seq += str(chiffre)

def print_seq(seq):
    print("Retenez la sequence")
    time.sleep(1)
    print(seq)
    time.sleep(3)
    os.system("clear")

print_seq(seq)
rep = input("Votre reponse : ")

while rep == seq:
    os.system("clear")
    score = score + 1
    print(f"Bonne reponse\nVotre score est : {score}")
    time.sleep(1)
    os.system("clear")
    chiffre = random.randint(0, 9)
    seq = seq + str(chiffre)
    print_seq(seq)
    rep = input("Votre reponse : ")

print(f"Mauvaise reponse, la sequence etait : {seq}")
print(f"Votre score final : {score}")




