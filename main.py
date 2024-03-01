# Description: Programme principal du logiciel de gestion
from fonctionAdmin import *

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()
loginadmin = curseur.execute('SELECT login FROM users WHERE role = "admin"').fetchall()
mdpadmin = curseur.execute('SELECT password FROM users WHERE role = "admin"').fetchall()
loguser = curseur.execute('SELECT login FROM users WHERE role != "admin"').fetchall()
mdpuser = curseur.execute('SELECT password FROM users WHERE role != "admin"').fetchall()


print('Bienvenue sur notre logiciel de gestion')

# Boucle pour la connexion de l'administrateur
compteur = 0
log = False
liste_user = []
liste_mdp = []
# Boucle principale du programme
while True:

    while compteur < 3 and log == False:
        compteur += 1
        if loguser and mdpuser:
            for logine, mdp in zip(loguser, mdpuser):

                liste_user.append(logine)
                liste_mdp.append(mdp)


            login = input('Login : ')
            password = input("Mot de passe : ")

            if login == loginadmin[0][0] and hashlib.sha256(password.encode()).hexdigest() == mdpadmin[0][0]:
                while True:
                    print('Bienvenue', loginadmin[0][0])
                    print('1. Ajouter un utilisateur')
                    print('2. Modifier un utilisateur')
                    print('3. Supprimer un utilisateur')
                    print('4. Lister les utilisateurs')
                    print('Q. Quitter')
                    choix = input('Votre choix : ')

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

            elif login in logine and hashlib.sha256(password.encode()).hexdigest() in mdp:
                print('Bienvenue', login)
                data = curseur.execute('SELECT * FROM users WHERE login = ?', (login,)).fetchall()
                for user_data in data:
                    nom = user_data[0]
                    prenom = user_data[1]
                    email = user_data[2]
                    num_tel = user_data[3]
                    role = user_data[4]
                    droit = user_data[5]
                user = User(nom, prenom, email, num_tel, role, droit)
                if user.get_role() == 'md':
                    print('Doc medecin 1')
                    print('Doc medecin 2')
                    print('Doc medecin 3')
                    input('Appuyez sur une touche pour continuer')
                elif user.get_role() == 'cm':
                    print('Commerciaux 1')
                    print('Commerciaux 2')
                    print('Commerciaux 3')
                    input('Appuyez sur une touche pour continuer')
                elif user.get_role() == 'etc':
                    print('Autre 1')
                    print('Autre 2')
                    print('Autre 3')
                    input('Appuyez sur une touche pour continuer')
                else:
                    print('Role inconnu')
                    input('Appuyez sur une touche pour continuer')



            else:
                print(f'Erreur de login ou de mot de passe. Il vous reste {3 - compteur} tentatives')

    if compteur == 3:
        print('Tentatives épuisées')
        exit()


