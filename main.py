
from graphical_fonction import *
import customtkinter as ctk

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()
# Récupération des logins et mots de passe pour l'administrateur
loginadmin = curseur.execute('SELECT login FROM users WHERE role = "admin"').fetchall()
mdpadmin = curseur.execute('SELECT password FROM users WHERE role = "admin"').fetchall()


if __name__ == '__main__':
    connexion_user()
    windows.mainloop()