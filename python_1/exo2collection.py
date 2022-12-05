# LISTES - ALGO : la valeur la plus petite
#V1
'''nom_chauffeur = ["Patrick", "Jean", "Georges", "Daniel"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9]
distancemin = distance_chauffeur_km[0]
index = 0
index_min = 0
for i in distance_chauffeur_km:
    if i <= distancemin:
        distancemin = i
        index_min = index
    index += 1
print(distancemin)
print(nom_chauffeur[index_min])'''

#OU

'''for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distancemin:
        distance_min = distance
        index_min = i'''

#V2
nom_et_dist = [("Patrick", 1.5), ("Jean", 0.4), ("Samuel", 10.5)]
print(nom_et_dist[0][1])

distancemin = nom_et_dist[0][1]
for i in range(len(nom_et_dist)):
    if nom_et_dist[i][1] < distancemin:
        distancemin = nom_et_dist[i][1]
        nom = nom_et_dist[i][0]
print(f"distance min : {distancemin}, chauffeur : {nom}")

#OU
'''nomdistancemin = nom_et_dist[0]
for a in nom_et_dist:
    if a[1] < nomdistancemin[1]:
        nomdistancemin = a'''