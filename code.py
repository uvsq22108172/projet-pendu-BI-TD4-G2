# random:le choix aleatoir d'un element à partir d'une liste
# unidecode: retourner une chaîne de caractères sans accents
from numpy import random
from unidecode import unidecode

# importer le dictionnaire de mots francais
liste_de_mots_francais = []
fichier_de_mots_francais = open('liste_fracais.txt', 'rt')
for m in fichier_de_mots_francais:
    liste_de_mots_francais.append(m.strip("\n"))

mot = liste_de_mots_francais[random.randint(0, len(liste_de_mots_francais)-1)]


# choisir la longueur du motjjjjjjjj


def longueur_du_mot(l,mot):
   l = int(input("choisir le nombre de lettre"))
   mot = liste_de_mots_francais[random.randint(0, len(liste_de_mots_francais)-1)]
   while len(mot) != l:
      mot = liste_de_mots_francais[random.randint(0, len(liste_de_mots_francais)-1)]
    return mot
      

# asterix: remplace les lettres par des *


def asterix(mot):
    r = '* ' * len(mot)
    return r[:-1]


# upper:retourner une chaîne de caractères en majuscules
# le “65” correspond au code ASCII de “A” et le “122” à celui de “z”
def saisie():
    lettre = input('Entrez une lettre : ')
    if len(lettre) > 1 or ord(lettre) < 65 or ord(lettre) > 122:
        return saisie()
    else:
        return lettre.upper()


def word():
    f = open('liste_fracais.txt', 'rt')
    contenu = f.readlines()
    return unidecode( choice(contenu) ).upper().replace('\n','')



lettres_deja_proposees = []

mot_a_deviner = word()

affichage = asterix( mot_a_deviner )

print( 'Mot à deviner : ' , affichage )

nb_erreurs = 0

while '*' in affichage and nb_erreurs < 11:
    lettre = saisie()
    if lettre not in lettres_deja_proposees:
        lettres_deja_proposees += [ lettre ]
        
    if lettre not in mot_a_deviner:
        nb_erreurs += 1
            
    affichage = asterix( mot_a_deviner , lettres_deja_proposees )
    print( '\nMot à deviner : ' , affichage , ' '*10 , 'Nombre d\'erreurs maximum :' , 11-nb_erreurs )