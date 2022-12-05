def poser_question(question):
    global score
    print("QUESTION")
    print("  " + question[0])
    for i in range(0,len(question[1])):
        print(f"  {i}-", question[1][i])
    print()
    reponse = input(f"Votre réponse (entre 0 et {int(len(question[1])) -1}) : ")
    try:
        if int(reponse) < 0 or int(reponse) >= int(len(question[1])):
            print(f"Rentrez un chiffre entre 0 et {int(len(question[1])) -1}")
            return poser_question(question)
        if question[2] == question[1][int(reponse)]:
            print("Bonne réponse")
            score += 1
        else:
            print("Mauvaise réponse")
    except:
        print(f"Rentrez un chiffre entre 0 et {int(len(question[1])) -1}")
        return poser_question(question)
        
    print()

def lancer_questionnaire(questionnaire):
    for i in questionnaire:
        poser_question(i)
    

score = 0

'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

#ici que se trouvent les donnees, separees du reste du code : donnes decorrelees de l'implementation
questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Landevant", "Mante la Jolie"), "Paris")
    ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
    ("Qu'est ce que j'ai mange a midi?", ("Pates", "Raviolis", "Jambon"), "Raviolis")
    )

lancer_questionnaire(questionnaire)

# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)
