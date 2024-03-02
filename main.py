# Description: Programme principal du logiciel de gestion

# Importation des fonction depuis fonctionAdmin.py
from fonctionAdmin import *

# connexion la base de données
connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()
# Récupération des logins et mots de passe pour l'administrateur
loginadmin = curseur.execute('SELECT login FROM users WHERE role = "admin"').fetchall()
mdpadmin = curseur.execute('SELECT password FROM users WHERE role = "admin"').fetchall()
# Récupération des logins et mots de passe pour les utilisateurs
loguser = curseur.execute('SELECT login FROM users WHERE role != "admin"').fetchall()
mdpuser = curseur.execute('SELECT password FROM users WHERE role != "admin"').fetchall()


print('Bienvenue sur notre logiciel de gestion')
# Initialisation des variables
compteur = 0
log = False
liste_user = []
liste_mdp = []
# Boucle principale du programme
while True:
    #Boucle pour la gestion des tentatives de connexion avec un compteur et une verif si on est connecté
    while compteur < 3 and log == False:
        compteur += 1
        # Récupération des logins et mots de passe pour les utilisateurs
        if loguser and mdpuser:
            for logine, mdp in zip(loguser, mdpuser):

                liste_user.append(logine)
                liste_mdp.append(mdp)


            login = input('Login : ')
            password = input("Mot de passe : ")
            # Vérification des identifiants de l'administrateur
            if login == loginadmin[0][0] and hashlib.sha256(password.encode()).hexdigest() == mdpadmin[0][0]:
                # Boucle pour la gestion des choix de l'administrateur
                while True:
                    print('Bienvenue', loginadmin[0][0])
                    print('1. Ajouter un utilisateur')
                    print('2. Modifier un utilisateur')
                    print('3. Supprimer un utilisateur')
                    print('4. Lister les utilisateurs')
                    print('Q. Quitter')
                    choix = input('Votre choix : ')
                    # Vérification du choix de l'administrateur avec un switch case qui renvoie vers les focntion de fonctionAdmin.py
                    match choix:
                        case '1':
                            add_user()
                        case '2':
                            update_user()
                        case '3':
                            delete_user()
                        case '4':
                            list_users()
                        case 'Q' | 'q':
                            print('Au revoir')
                            break
                            log = False
                        case _:
                            print('Choix invalide')
                    log = True
            # Vérification des identifiants des utilisateurs
            elif login in logine and hashlib.sha256(password.encode()).hexdigest() in mdp:
                print('Bienvenue', login)
                # Récupération des données de l'utilisateur connecté
                data = curseur.execute('SELECT * FROM users WHERE login = ?', (login,)).fetchall()
                # Instanciation d'un objet User avec les données récupérées de la base de données pour pouvoir interagir avec les méthodes de la classe User
                for user_data in data:
                    nom = user_data[0]
                    prenom = user_data[1]
                    email = user_data[2]
                    num_tel = user_data[3]
                    role = user_data[4]
                    droit = user_data[5]
                user = User(nom, prenom, email, num_tel, role, droit)

                # affichage des documents en fonction du role de l'utilisateur
                if user.get_role() == 'md':
                    print('Doc medecin 1')
                    print('Doc medecin 2')
                    print('Doc medecin 3')
                    input('Appuyez sur la touche entrer pour continuer')
                elif user.get_role() == 'cm':
                    print('Commerciaux 1')
                    print('Commerciaux 2')
                    print('Commerciaux 3')
                    input('Appuyez sur la touche entrer pour continuer')
                elif user.get_role() == 'etc':
                    print('Autre 1')
                    print('Autre 2')
                    print('Autre 3')
                    input('Appuyez sur la touche entrer pour continuer')
                else:
                    print('Role inconnu')
                    input('Appuyez sur la touche entrer pour continuer')



            else:
                print(f'Erreur de login ou de mot de passe. Il vous reste {3 - compteur} tentatives')
    # Si le compteur est égal à 3, on sort de la boucle
    if compteur == 3:
        print('Tentatives épuisées')
        exit()


