# Pierre feuille ciseau jusqu'a ce que le joueur gagne
import random

def game():
    user = input("What's your choice ?\n - r : rock\n - p : paper\n - s : scissors\n -> ")
    comp = random.choice("rps")
    if user == comp:
        print(f"{user} VS {comp} : Tie ! Try again")
        return game()
    elif (user == "s" and comp == "p") or (user == "p" and comp == "r") or (user == "r" and comp == "s"):
        print(f"{user} VS {comp} : ", end = "")
        return True
    else:
        print(f"{user} VS {comp} : ", end = "")
        return False

#r > s, s > p, p > r
while game() != 1:
    print("You lost, try again")
print("You won, congrats!")
