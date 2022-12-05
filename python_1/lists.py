from logging.config import listen


friends = ["Manon", "Edwige", "Elouan"]
nombre = [1, 2, 3, 4]
friends.extend(nombre) #ajoute liste apres autre liste
friends.append("Manon") #ajoute un element fin liste
friends.insert(1, "Yo gros") # ajoute un element a lindex qu on veut ds liste
friends.remove("Manon") #enleve elemtn au on veut
friends.clear() #supp toute la liste
friends.pop() #supp dernier element list
friends.index("Edwige") #donne index si nom dans liste
friends.count("Manon") #donne le nb de fois nom apparait liste
friends.sort() #tri liste ascendant
friends.reverse() #inverse liste
friends2 = friends.copy() #copie liste 