from fonctionAdmin import *
from graphical import *

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()
# Récupération des logins et mots de passe pour l'administrateur
loginadmin = curseur.execute('SELECT login FROM users WHERE role = "admin"').fetchall()
mdpadmin = curseur.execute('SELECT password FROM users WHERE role = "admin"').fetchall()
# Récupération des logins et mots de passe pour les utilisateurs
loguser = curseur.execute('SELECT login FROM users WHERE role != "admin"').fetchall()
mdpuser = curseur.execute('SELECT password FROM users WHERE role != "admin"').fetchall()



connexion_user(loginadmin,mdpadmin)