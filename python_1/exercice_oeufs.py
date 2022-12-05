import time
from math import *

print("- Oeufs a la coque : 3 minutes")
print("- Oeufs mollets : 6 minutes")
print("- Oeufs durs : 9 minutes")

def affiche_point():
    for i in range (0, 9):
        time.sleep(1)
        print(".", end ="", flush = True)
    print("\n", end = "")
tps = input("Option choisie : ")
sec = int(tps) * 60
affiche_point()
total = sec - 10
tpstotal = total
for j in range (0, tpstotal):
    for k in range (0, 9):
        nbmin = total / 60
        nbminarr = floor(nbmin)
        nbsec = total % 60
        print(f"Duree restante : {nbminarr:0>2d}:", end="")
        print(f"{nbsec:02d}", end = "")
        time.sleep(1)
        affiche_point()
        total = total - 10
        if total == 0 :
            break
    if total == 0 :
        break
print("CUISSON TERMINEE")
