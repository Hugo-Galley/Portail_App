from User import *
import getpass
from fonctionAdmin import *

loginadmin = 'admin'
mdpadmin = 'admin'

print('Bienvenue sur notre logiciel de gestion')

# Boucle pour la connexion de l'administrateur
while True:
    login = input('Login : ')
    password = input("Mot de passe : ")
    
    if login == loginadmin and password == mdpadmin:
        print('Bienvenue', loginadmin)
        break  # Sortir de la boucle une fois que l'administrateur est connecté
    else:
        print('Erreur de login ou de mot de passe')

# Boucle principale du programme
while True:
    print('1. Ajouter un utilisateur')
    print('2. Modifier un utilisateur')
    print('3. Supprimer un utilisateur')
    print('4. Lister les utilisateurs')
    print('0. Quitter')
    choix = input('Votre choix : ')

    if choix == '1':
        add_user()
    elif choix == '2':
        update_user()
    elif choix == '3':
        delete_user()
    elif choix == '4':
        list_users()
    elif choix == '0':
        print('Au revoir')
        break  # Sortir de la boucle principale
    else:
        print('Choix invalide')
