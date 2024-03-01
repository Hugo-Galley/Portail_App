from User import *
import getpass
from fonctionAdmin import *

loginadmin = 'admin'
mdpadmin = 'admin'

print('Bienvenue sur notre logiciel de gestion')

# Boucle pour la connexion de l'administrateur
compteur = 0
log = False
# Boucle principale du programme
while True:

    while compteur < 3 and log == False:
        compteur += 1
        login = input('Login : ')
        password = input("Mot de passe : ")

        if login == loginadmin and password == mdpadmin:
            print('Bienvenue', loginadmin)
            log = True
        else:
            print(f'Erreur de login ou de mot de passe. Il vous reste {3 - compteur} tentatives')

    if compteur == 3:
        print('Tentatives épuisées')
        exit()
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
        log = False
    else:
        print('Choix invalide')
