# code du jeu pendu
import random

# liste de listes de mots avec nombre de lettres croissant 0 , 1, 2, 3, 5...
L = [[], [], [], [], [], ['ACTIF','AVENU'], ['WHISKY', 'COCCYX'], ['ACCOLAT', 'ACCOLEE'],['ABOUTIES','ZOOLOGIE'], ['ABDOMINAL','VAISSELLE']]

# CHOIX de longueur du mot
longueur_de_mot = int(input("nobre de lettre"))

# Le choix aleatoire du mot avec nombre de lettres predefini
mot_a_deviner = random(L[longueur_de_mot])

# Cacher le mot à deviner par des astérix
asterix = '* ' * len(mot_a_deviner)
print(asterix)

# Choix du nombres de tentatives autorisées
tentatives = int(input('nobres de tentatives'))
erreurs = 0

while asterix != mot_a_deviner and erreurs < tentatives:
    lettre = input("Entrez une lettre : ")
    for i in range(len(mot_a_deviner)):
        if lettre == mot_a_deviner[i]:
            asterix = asterix[:i] + lettre + asterix[i+1:]
    print(asterix)

if mot_a_deviner == asterix and erreurs < tentatives:
    print('Bravo ! Le mot', mot_a_deviner, 'a été trouvé')
else:
    print('vous avez perdu! Le mot', mot_a_deviner, 'n a pas etait retrouvé')
