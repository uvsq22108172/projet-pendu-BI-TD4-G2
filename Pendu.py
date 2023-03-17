#Marche pas y'a encore des choses a debug


import random
Mots = ["informatique", "biologie", "chimie"]

def Afficher_mot(mot_aléatoire, lettres_trouvées) :
    print("mot_aléatoire", end = '')
    for i in range(len(mot_aléatoire)) :
        if mot_aléatoire[i] in lettres_trouvées :
            print(" ", mot_aléatoire[i], " ", end = '')
        else :
            print(" * ", end = '')
    
    print() #espace

def Mot_trouvé(mot_aléatoire, lettres_trouvées) :
    for i in range(len(mot_aléatoire)) :
        if mot_aléatoire[i] not in lettres_trouvées :
            return False
    
    return True

def Principale(Mots) :
    mot_aléatoire = random.choice(Mots)
    print(mot_aléatoire)
    tentatives_restantes = 7
    lettres_trouvées = set()  #ensemble
    
    while tentatives_restantes > 0 :
        Afficher_mot(mot_aléatoire, lettres_trouvées)
        print("Il te reste", tentatives_restantes, "tentatives")
        lettre = input("Choisis ta lettre : ")

        if lettre not in Mots :
            tentatives_restantes -= 1

        elif lettre in Mots and lettre not in lettres_trouvées :
            lettres_trouvées.add(lettre)

        elif Mot_trouvé(mot_aléatoire, lettres_trouvées) :
            print("Bravo tu as trouvé le mot, veux-tu rejouer ?")
            print(mot_aléatoire)
            break

        elif tentatives_restantes == 0 :
            print("Tu as perdu, veux-tu réessayer ?")
            break
    return

Principale(Mots)
