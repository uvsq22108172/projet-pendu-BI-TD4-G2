import tkinter
import tkinter as tk                                                
from tkinter import *
#import pygame
#import subprocess

graphique = tkinter.Tk()                                   
graphique.geometry("1920x1080")                                 
graphique.title("Pendu BI-TD4_Groupe 2")
mainmenu = tkinter.Menu(graphique)

label = Label(text= "Jeu du Pendu")                                     
label.pack(pady=100) 

aide1 = None       #variable globale 

def aide_pendu() :
    global aide1  #référence variable globale
    aide1 = tkinter.Tk()
    label_aide = Label(aide1, text= "Insérer les règles ici")
    label_aide.pack(pady= 250)
    aide1.geometry("1920x1080")
    bouton_leave = Button(aide1, text="Revenir au menu principale", command= (exit_aide))
    bouton_leave.pack(pady=100)

def exit_aide() :
    global aide1 #référence variable globale
    aide1.destroy()

    

    
#---------------------------------------------------------------------------------------------------------------------
# source : https://learntutorials.net/fr/pygame/topic/7419/ajout-de-musique-de-fond-et-d-effets-sonores
#def paramètres_button() :
    #son = Label(command=change_volume)
    #son.pack()

#def open_volume_window() :
    #volume_window = tk.Toplevel(graphique)
    #volume_window.title("Réglage du volume")

#def change_volume(volume) :
    #pygame.mixer.music.set_volume(volume)
    

#def change_vol() :
    #volume_var = tk.DoubleVar() #créer une variable qui peut stocker et gérer des valeurs de type flottante
    #volume_var.set(0.5) 
    #volume_menu = tk.OptionMenu(graphique, volume_var, *[(label, value) for label, value in VOLUME_OPTIONS], command=lambda v: change_volume(v[1]))
    #olume_menu.pack(side=LEFT)


# Initialisation de pygame pour jouer de la musique
#pygame.mixer.init()
#music_file = r"C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Background sonore Pendu\No copyright Song.mp3"
#pygame.mixer.music.load(music_file)
#pygame.mixer.music.play(-1)      #loop

#VOLUME_OPTIONS = [("Mute", 0.0), ("Faible", 0.2), ("Moyen", 0.5), ("Elevé", 1.0)] 


#---------------------------------------------------------------------------------------------------------------------
#def Jouer() :
    #programme = r"" 
    #subprocess.Popen(["python",chemin d'accès du fichier pendu])

bouton_play = Button(text="Jouer", command="jouer")    
bouton_play.pack()                                              

bouton_leave = Button(text="Quitter", command=(quit))
bouton_leave.pack(pady=200)

paramètres = tkinter.Menu(mainmenu)                        
paramètres.add_radiobutton(label= 'Volume Sonore', command="change_vol")
mainmenu.add_cascade(label= 'Paramètres', menu= paramètres)  

aide = tkinter.Menu(mainmenu)
aide.add_radiobutton(label= 'Aide', command=(aide_pendu))
mainmenu.add_cascade(label= 'Aide', menu= aide)

   

graphique.config(menu=mainmenu)
graphique.mainloop()