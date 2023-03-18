#Début de l'interface graphique
import pygame
import tkinter
import tkinter as tk                                                
from tkinter import *
import subprocess


graphique = tkinter.Tk()                                       
graphique.geometry("1920x1080")                                 
graphique.title("Pendu BI-TD4_Groupe 2")
mainmenu = tkinter.Menu(graphique)


label = Label(text= "Jeu du Pendu")                                     
label.pack(pady=100)                                            

#---------------------------------------------------------------------------------------------------------------------

def paramètres_button() :
    son = Label(command=change_volume)
    son.pack()

def open_volume_window():
    volume_window = tk.Toplevel(graphique)
    volume_window.title("Réglage du volume")

def change_volume(volume):
    pygame.mixer.music.set_volume(volume)

def change_vol() :
    volume_var = tk.DoubleVar()
    volume_var.set(0.5) 
    volume_menu = tk.OptionMenu(graphique, volume_var, *[(label, value) for label, value in VOLUME_OPTIONS], command=lambda v: change_volume(v[1]))
    volume_menu.pack(side=LEFT)


# Initialisation de pygame pour jouer de la musique
pygame.mixer.init()
music_file = r"C:\Fac\L1 Semestre 2\IN200N\projet-pendu-BI-TD4-G2-main\Background sonore Pendu\No copyright Song.mp3"
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

VOLUME_OPTIONS = [("Mute", 0.0), ("Faible", 0.2), ("Moyen", 0.5), ("Elevé", 1.0)]


#---------------------------------------------------------------------------------------------------------------------
#def Jouer() :
    #programme = r"" 
    #subprocess.Popen(["python",chemin d'accès du fichier pendu])

bouton_play = Button(text="Jouer", command=(Jouer))            #Remplacer cette ligne par : bouton_play = Button(text="Jouer", command="jouer") ; et lancer l'interface
bouton_play.pack()                                              

bouton_leave = Button(text="Quitter", command=(quit))
bouton_leave.pack(pady=200)

paramètres = tkinter.Menu(mainmenu)                        
paramètres.add_radiobutton(label= 'Volume Sonore', command=(change_vol))

mainmenu.add_cascade(label= 'Paramètres', menu= paramètres)      

graphique.config(menu=mainmenu)
graphique.mainloop()                                            