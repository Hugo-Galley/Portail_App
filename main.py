# Description: Fichier principal du programme qui permet de lancer la fenêtre de connexion
# importation des modules
from graphical_fonction import *
import customtkinter as ctk

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()
# Récupération des logins et mots de passe pour l'administrateur
loginadmin = curseur.execute('SELECT login FROM users WHERE role = "admin"').fetchall()
mdpadmin = curseur.execute('SELECT password FROM users WHERE role = "admin"').fetchall()

# Lancement de la fenêtre de connexion
if __name__ == '__main__':
    connexion_user()
    windows.mainloop()