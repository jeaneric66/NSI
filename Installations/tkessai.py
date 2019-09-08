#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:35:23 2017

@author: jeanericrichard
"""

from tkinter import *

# Création de la fenêtre principale (main window)
Mafenetre = Tk()

# Création d'un widget Label (texte 'Bonjour tout le monde !')
Label1 = Label(Mafenetre, text = 'Bonjour tout le monde !', fg = 'red')
# Positionnement du widget avec la méthode pack()
Label1.pack()

# Création d'un widget Button (bouton Quitter)
Bouton1 = Button(Mafenetre, text = 'Quitter', command = Mafenetre.destroy)
Bouton1.pack()

# Lancement du gestionnaire d'événements
Mafenetre.mainloop()