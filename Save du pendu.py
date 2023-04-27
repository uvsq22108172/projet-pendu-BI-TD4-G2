import tkinter
import tkinter as tk                                                
from tkinter import *
import random
import pygame
from PIL import Image,ImageTk

graphique = tk.Tk()                                   
graphique.geometry("1920x1080")                                 
graphique.title("Pendu BI-TD4_Groupe 2")
mainmenu = tkinter.Menu(graphique)

bg = tk.PhotoImage(file= "C:/Fac/L1 Semestre 2/IN200N/IMAGES PENDU/bgpendu.png")
bg_label = tk.Label(graphique, image= bg)
bg_label.configure(width=graphique.winfo_width(),height=graphique.winfo_height())


label = Label(text= "Jeu du Pendu")                                     
label.pack(pady=100)

aide1 = None

def aide_pendu() :
    global aide1  #référence variable globale
    aide1 = tk.Tk()
    label_aide = Label(aide1, text= "Le but du jeu est simple : deviner toute les lettres qui doivent composer un mot en un nombre limité de tentatives. A chaque fois que le joueur devine une lettre, celle-ci est affichée. Dans le cas contraire, le dessin d'un pendu se met à apparaître…")
    label_aide.pack(pady= 250)
    aide1.geometry("1920x1080")
    bouton_leave = Button(aide1, text="Revenir au menu principale", command= (exit_aide))
    bouton_leave.pack(pady=100)

def exit_aide() :
    global aide1 #référence variable globale
    aide1.destroy()

# définir la longueuer des mots
# Fonction pour obtenir la valeur sélectionnée dans le menu déroulant(longueuer de mot)
def word_length() :
    global entier
    entier = entier_var.get()
    valeur_label.config(text="Le nombre de lettres choisi : " + str(entier))


# Création du menu déroulant pour choisir un entier
entier_var = tk.IntVar()
entier_var.set(8)  # Valeur par défaut : 6 lettres
entier_menu = tk.OptionMenu(graphique, entier_var, 6, 7, 8, 9, 10)
entier_menu.pack()

# Création d'un bouton pour valider le choix du nombre de lettres
choisir_entier_btn = tk.Button(graphique, text="Confirmer le nombre de lettres", command=word_length)
choisir_entier_btn.pack()

# Création d'un label pour afficher la valeur choisie
valeur_label = tk.Label(graphique, text="")
valeur_label.pack()

# Nombres d'échecs
# Fonction pour obtenir la valeur sélectionnée dans le menu déroulant
def attempts_allowed():
    global number
    number = number_var.get()
    val_label.config(text="Le nombres d'erreurs autorisés  est de : " + str(number))


# Création du menu déroulant pour choisir un entier(nombre d'erreurs)
number_var = tk.IntVar()
number_var.set(7)  # Valeur par défaut : 7
number_menu = tk.OptionMenu(graphique, number_var, 5, 7, 9)
number_menu.pack()

# Création d'un bouton pour valider le choix de l'entier
choisir_number_btn = tk.Button(graphique, text="Confirmer le nombre de tentatives", command=attempts_allowed)
choisir_number_btn.pack()

# Création d'un label pour afficher la valeur choisie
val_label = tk.Label(graphique, text="")
val_label.pack()


def jeu_du_pendu() :
    #sources : http://lycee.lagrave.free.fr/isn/projet/8_projet_pendu_GUI_tkinter.html, https://www.mathweb.fr/euclide/2020/09/07/le-jeu-du-pendu-en-python/, https://www.youtube.com/watch?v=ITDo4OkI6mk&ab_channel=CharlieCode, https://openclassrooms.com/forum/sujet/jeu-pendu-avec-tkinter
    
    #images = ["C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Dessin pendu\erreur1", #images du pendu
     #"C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Dessin pendu\erreur2", 
    #"C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Dessin pendu\erreur3", 
    #"C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Dessin pendu\erreur4", 
    #"C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Dessin pendu\erreur5", 
    #"C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Dessin pendu\erreur6", 
    #"C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Dessin pendu\erreur7"]
    
    def choix_du_mot() :
        mots = [['touche', 'joyeux'], ['docteur', 'ajdoint'], ['biologie', 'absorber'], ['abdominal', 'zymologie'], ['architecte', 'professeur']]
        return random.choice(mots[entier-6])

    def vérification(lettre, mot, mot_caché) :                              #vérifie si la lettre est dans le mot
        for i in range(len(mot)) :                                          #parcourt tout le mot selon son nombre de lettre grace a "len"
            if mot[i] == lettre :                                           #vérifie si la lettre entrée est la meme que la lettre actuelle dans la boucle
                mot_caché = mot_caché[:i] + lettre + mot_caché[i+1:]        #met a jour la variable mot_caché pour remplacer la lettre correspondante a la lettre donnée, remplace  la lettre à l'index i par la lettre donnée, on obtient une nouvelle chaîne de caractères affectée à la variable "mot_caché"
        return mot_caché                                                    #renvoie la variable mot_caché qui est mise a jour, contient le mot caché avec la lettre donnée remplacée si elle était présente

    def montrer_mot_caché(mot_caché) :             #prend mot_caché et ajoute des espaces entre les lettres pour améliorer la lisibilité
        return ' '.join(mot_caché)

    
    global tentatives_restantes
    
    jeu = tk.Tk()
    jeu.geometry('1920x1080')
    
    label_mot = tk.Label(jeu, text='')
    label_mot.pack(pady=100)

    label_tentatives_restantes = tk.Label(jeu, text='Nombre de tentatives restantes:' + str(number))
    label_tentatives_restantes.pack(pady=50)

    entry_lettre = tk.Entry(jeu)
    entry_lettre.pack()

    bouton_deviner = tk.Button(jeu, text='Deviner')
    bouton_deviner.pack(pady=80)

    global tentatives_restantes, mot_caché
    
    mot = choix_du_mot()
    mot_caché = '*' * len(mot)
    tentatives_restantes = number
    
    def deviner_une_lettre() :                           #fonction qui gère une tentative "gagnante" ou "perdante" 
        global tentatives_restantes, mot_caché
        lettre = entry_lettre.get().lower()              #récupère entry_lettre et la stocke dans la variable lettre; .lower() pour mettre les lettres en minuscule pour éviter des erreurs
        entry_lettre.delete(0, tk.END)                   #efface le contenu de entry_lettre pour permettre une nouvelle entrée
        if lettre in mot :                               #boucle if qui vérifie si la lettre entrée est dans le mot
            mot_caché = vérification(lettre, mot, mot_caché)        #si lettre dans le mot : appelle la fonction vérification  et met a jour mot_caché en remplacant les étoiles par la lettre trouvée
            label_mot.config(text=montrer_mot_caché(mot_caché))     #met a jour le label mot en utilisant la fonction montrer_mot_caché
            if '*' not in mot_caché :                    #vérifie qu'il n'y a plus d'étoiles donc de lettres a trouver pour gagner
                label_tentatives_restantes.config(text='Vous avez gagné !')    #si aucune étoile : label des tentatives_restantes est mis a jour
                bouton_deviner.config(state=tk.DISABLED)                       #le bouton deviner est désactivé car la partie est finie
        else:                                           #si la lettre entrée n'est pas dans le mot :
            tentatives_restantes -= 1                   #le joueur perd une tentative
            label_tentatives_restantes.config(text=f'Nombre de tentatives restantes: {tentatives_restantes}') #met a jout le nombre de tentatives qu'il reste au joueur
            if tentatives_restantes == 0:               #si le joueur n'a plus aucune tentative restante :
                label_mot.config(text=mot)              #affiche le mot qui était a deviner si le joueur a perdu
                label_tentatives_restantes.config(text='Vous avez perdu !')         #indique que le joueur a perdu
                bouton_deviner.config(state=tk.DISABLED)            #le bouton deviner est désactivé, il ne reste plus qu'a rejouer ou quitter

    #def rejouer() :
        #global mot, mot_caché, tentatives_restantes
        #mot = choix_du_mot()
        #mot_caché = '*' * len(mot)
        #tentatives_restantes = 7
        #label_mot.config(text=montrer_mot_caché(mot_caché))
        #label_tentatives_restantes.config(text=f'Nombre de tentatives restantes: {tentatives_restantes}')
        #bouton_deviner.config(state=tk.NORMAL)
    
    def rejouer() :
        jeu.destroy()
        jeu_du_pendu()
    bouton_rejouer = tk.Button(jeu, text='Rejouer', command=rejouer)
    bouton_rejouer.pack()      
    

# Configuration du bouton pour appeler la fonction de gestion des tentatives
    bouton_deviner.config(command=deviner_une_lettre)
    
# Affichage du mot caché
    label_mot.config(text=montrer_mot_caché(mot_caché))

    def exit_jeu() :
        jeu.destroy()
    
    bouton_quitter_jeu = Button(jeu, text="Revenir au menu principale", command=(exit_jeu))
    bouton_quitter_jeu.pack(pady= 100)

def jeu_du_pendu_aléatoire() :

    def choix_du_mot() :
        global mots_aléatoire
        mots_aléatoire = ['manger', 'docteur', 'effacer', 'xylophone', 'guitare']
        return random.choice(mots_aléatoire)
    

    def vérification(lettre, mot, mot_caché) :           #vérifie si la lettre est dans le mot
        for i in range(len(mot)) :
            if mot[i] == lettre :                        
                mot_caché = mot_caché[:i] + lettre + mot_caché[i+1:]
        return mot_caché

    def montrer_mot_caché(mot_caché) :             #met des espaces entre les lettres
        return ' '.join(mot_caché)

    global tentatives_restantes
    
    jeu = tk.Tk()
    jeu.geometry('1920x1080')
    
    label_mot = tk.Label(jeu, text='')
    label_mot.pack(pady=100)

    label_tentatives_restantes = tk.Label(jeu, text='Nombre de tentatives restantes: 7')
    label_tentatives_restantes.pack(pady=50)

    entry_lettre = tk.Entry(jeu)
    entry_lettre.pack()

    bouton_deviner = tk.Button(jeu, fg="blue", text='Deviner')
    bouton_deviner.pack(pady=80)

    global tentatives_restantes, mot_caché
    
    mot = choix_du_mot()
    mot_caché = '*' * len(mot)
    tentatives_restantes = 7
    

    def deviner_une_lettre() :                           #fonction qui gère une tentative "gagnante" ou "perdante" 
        global tentatives_restantes, mot_caché
        lettre = entry_lettre.get().lower()
        entry_lettre.delete(0, tk.END)
        if lettre in mot :
            mot_caché = vérification(lettre, mot, mot_caché)
            label_mot.config(text=montrer_mot_caché(mot_caché))
            if '*' not in mot_caché :
                label_tentatives_restantes.config(text='Vous avez gagné !')
                bouton_deviner.config(state=tk.DISABLED)
        else:
            tentatives_restantes -= 1
            label_tentatives_restantes.config(text=f'Nombre de tentatives restantes: {tentatives_restantes}')
            if tentatives_restantes == 0:
                label_mot.config(text=mot)
                label_tentatives_restantes.config(text='Vous avez perdu !')
                bouton_deviner.config(state=tk.DISABLED)

    def ajouter_mot():
        nouveau_mot = entree_mot.get()
        if nouveau_mot != '':
            mots_aléatoire.append(nouveau_mot)
            label_confirmation.config(text=f'Le mot "{nouveau_mot}" a été ajouté à la liste !')
            entree_mot.delete(0, tk.END)
        else:
            label_confirmation.config(text='Veuillez entrer un mot.')
    
    label_entree = tk.Label(jeu, text='Entrez un nouveau mot :')
    label_entree.pack()

    entree_mot = tk.Entry(jeu)
    entree_mot.pack(pady=10)

    bouton_ajouter = tk.Button(jeu, text='Ajouter', command=ajouter_mot)
    bouton_ajouter.pack(pady=10)

    label_confirmation = tk.Label(jeu, text='')
    label_confirmation.pack(pady=10)
        
    def dessin_pendu():
        canvas = Canvas(jeu, width=Image_1.width(), height=Image_2.height())
        canvas.pack(side= LEFT)
        Image_1= Image.open("C:/Fac/L1 Semestre 2/IN200N\IMAGES PENDU/imagependu0.png")
        Image_2= Image.open("C:/Fac/L1 Semestre 2/IN200N\IMAGES PENDU/imagependu1.png")
        Image_3= Image.open("C:/Fac/L1 Semestre 2/IN200N\IMAGES PENDU/imagependu2.png")
        Image_4= Image.open("C:/Fac/L1 Semestre 2/IN200N\IMAGES PENDU/imagependu3.png")
        Image_5= Image.open("C:/Fac/L1 Semestre 2/IN200N/IMAGES PENDU/imagependu4.png")
        Image_6= Image.open("C:/Fac/L1 Semestre 2/IN200N/IMAGES PENDU/imagependu5.png")
        Image_7= Image.open("C:/Fac/L1 Semestre 2/IN200N/IMAGES PENDU/imagependu6.png")
        Image_8= Image.open("C:/Fac/L1 Semestre /\IN200N/IMAGES PENDU/imagependu7.png")
        photo1 = ImageTk.PhotoImage(Image_1)
        photo2 = ImageTk.PhotoImage(Image_2)
        photo3 = ImageTk.PhotoImage(Image_3)
        photo4 = ImageTk.PhotoImage(Image_4)
        photo5 = ImageTk.PhotoImage(Image_5)
        photo6 = ImageTk.PhotoImage(Image_6)
        photo7= ImageTk.PhotoImage(Image_7)
        photo8= ImageTk.PhotoImage(Image_8)
        if tentatives_restantes == 7 :
            canvas.create_image(0, 0, anchor=NW, image=photo1)
        if tentatives_restantes == 6 :
            canvas.create_image(0, 0, anchor=NW, image=photo2)
        if tentatives_restantes == 5 :
            canvas.create_image(0, 0, anchor=NW, image=photo3)
        if tentatives_restantes == 4 :
            canvas.create_image(0, 0, anchor=NW, image=photo4)
        if tentatives_restantes == 3 :
            canvas.create_image(0, 0, anchor=NW, image=photo5)
        if tentatives_restantes == 2 :
            canvas.create_image(0, 0, anchor=NW, image=photo6)
        if tentatives_restantes == 1 :
            canvas.create_image(0, 0, anchor=NW, image=photo7)
        if tentatives_restantes == 0 :
            canvas.create_image(0, 0, anchor=NW, image=photo8)
        im = PhotoImage(file=Image_1)
        dessin_pendu.create_image(x=0, y=100, image = im)
        
   



   
    def rejouer() :
        jeu.destroy()
        jeu_du_pendu_aléatoire()
    bouton_rejouer = tk.Button(jeu, text='Rejouer', fg="green", command=rejouer)
    bouton_rejouer.pack()      

# Configuration du bouton pour appeler la fonction de gestion des tentatives
    bouton_deviner.config(command=deviner_une_lettre)
    
# Affichage du mot caché
    label_mot.config(text=montrer_mot_caché(mot_caché))

    def exit_jeu() :
        jeu.destroy()
    
    bouton_quitter_jeu = Button(jeu, text="Revenir au menu principale", fg= "red", command=(exit_jeu))
    bouton_quitter_jeu.pack(pady= 30)

#---------------------------------------------------------------------------------------------------------------------
# source : https://learntutorials.net/fr/pygame/topic/7419/ajout-de-musique-de-fond-et-d-effets-sonores
def paramètres_button() :
    son = Label(command=change_volume)
    son.pack()

def open_volume_window() :
    volume_window = tk.Toplevel(graphique)
    volume_window.title("Réglage du volume")

def change_volume(volume) :
    pygame.mixer.music.set_volume(volume)
    

def change_vol() :
    volume_var = tk.DoubleVar() #créer une variable qui peut stocker et gérer des valeurs de type flottante
    volume_var.set(0.5) 
    volume_menu = tk.OptionMenu(graphique, volume_var, *[(label, value) for label, value in VOLUME_OPTIONS], command=lambda v: change_volume(v[1]))
    volume_menu.pack(side=LEFT)


# Initialisation de pygame pour jouer de la musique
pygame.mixer.init()
music_file = r"C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Background sonore Pendu\No copyright Song.mp3"
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)      #loop

VOLUME_OPTIONS = [("Mute", 0.0), ("Faible", 0.2), ("Moyen", 0.5), ("Elevé", 1.0)] 

#--------------------------------------------------------------------------------------------------------------------


bouton_play = Button(text="Jouer",fg="blue", command=(jeu_du_pendu))    
bouton_play.pack()                                         

bouton_play_2 = Button(text="Jouer Aléatoire",fg="green", command=(jeu_du_pendu_aléatoire))
bouton_play_2.pack()



bouton_leave = Button(text="Quitter",fg= "red", command=(quit))
bouton_leave.pack(pady=100)

paramètres = tkinter.Menu(mainmenu)                        
paramètres.add_radiobutton(label= 'Volume Sonore', command=(change_vol))
mainmenu.add_cascade(label= 'Paramètres', menu= paramètres)  

score_button = tkinter.Menu(mainmenu)
score_button.add_radiobutton(label= 'Score',command= "test")
mainmenu.add_cascade(label='Score')

aide = tkinter.Menu(mainmenu)
aide.add_radiobutton(label= 'Aide', command=(aide_pendu))
mainmenu.add_cascade(label= 'Aide', menu= aide)


graphique.config(menu=mainmenu)

graphique.mainloop()