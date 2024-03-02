# Description: Ce fichier contient les fonctions qui permettent d'ajouter, modifier, supprimer et lister les utilisateurs
# Importation des modules
from User import *
import hashlib
import sqlite3
# Connexion à la base de données
connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()
# Initialisation des variables
liste_user = []
def add_user():
    print('Ajout d\'un utilisateur')
    # Instancier un nouvel objet User avec les données saisies par l'administrateur
    user = User(input('Nom : '),input('Prenom : '),input('Email : '),input('Numéro de téléphone : '),input('Droit (md : medecin, cm = commerciaux, etc = autre) :'),input('Droit (r : Ecrire, w : lire ) :'))
    # Générer un login et un mot de passe pour l'utilisateur
    user.genrate_login()
    user.generate_password(input('Nombre de caractères pour le mot de passe : '))
    # Ajouter l'utilisateur à la base de données
    curseur.execute('INSERT INTO users (nom, prenom, email, num_tel, role, droit,login, password) VALUES (?,?,?,?,?,?,?,?)', (user.get_nom(), user.get_prenom(), user.get_email(), user.get_num_tel(), user.get_role(), user.get_droit(), user.get_login(), hashlib.sha256(user.get_password().encode()).hexdigest()))
    connexion.commit()
    # Afficher un message de succès avec le login et le mot de passe de l'utilisateur
    print(f'Utilisateur ajouté avec succès dont le login est {user.get_login()} et le mot de passe est {user.get_password()}')
    return False
def update_user():
    login = input('Login de l\'utilisateur à modifier : ')

    # Récupérer les données de l'utilisateur à modifier
    data = curseur.execute('SELECT * FROM users WHERE login = ?', (login,)).fetchall()
    user_trouve = False
    for user_data in data:
        # Vérifier si l'utilisateur existe
        if user_data[7] == login:
            user_trouve = True
            # Instancier un nouvel objet User avec les données récupérées de la base de données
            user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6])
            # Demander à l'administrateur de saisir le champ à modifier
            choix = input('1. Modifier le nom\n2. Modifier le prénom\n3. Modifier l\'email\n4. Modifier le numéro de téléphone\n5. Modifier le rôle\n6. Modifier le droit\n7. Modifier le mot de passe\n8. Modifier le login\nVotre choix : ')
            # Modifier le champ choisi par l'administrateur et mettre à jour la base de données
            if choix == '1':
                user.set_nom(input('Nouveau nom : '))
                curseur.execute('UPDATE users SET nom = ? WHERE login = ?', (user.get_nom(), login))
            elif choix == '2':
                user.set_prenom(input('Nouveau prénom : '))
                curseur.execute('UPDATE users SET prenom = ? WHERE login = ?', (user.get_prenom(), login))
            elif choix == '3':
                user.set_email(input('Nouvel email : '))
                curseur.execute('UPDATE users SET email = ? WHERE login = ?', (user.get_email(), login))
            elif choix == '4':
                user.set_num_tel(input('Nouveau numéro de téléphone : '))
                curseur.execute('UPDATE users SET num_tel = ? WHERE login = ?', (user.get_num_tel(), login))
            elif choix == '5':
                user.set_role(input('Nouveau rôle : '))
                curseur.execute('UPDATE users SET role = ? WHERE login = ?', (user.get_role(), login))
            elif choix == '6':
                # Vérifier si le droit est valide et mettre à jour la base de données
                while True:
                    user.droit = input('Nouveau droit : (md : medecin, cm = commerciaux, etc = autre) : ')
                    if user.droit not in ['md', 'cm', 'etc']:
                        print('Choix invalide')
                    else:
                        break

                curseur.execute('UPDATE users SET droit = ? WHERE login = ?', (user.droit, login))

            elif choix == '7':
                user.generate_password(input('Nombre de caractères pour le mot de passe :'))
                curseur.execute('UPDATE users SET password = ? WHERE login = ?', (hashlib.sha256(user.get_password().encode()).hexdigest(), login))
            elif choix == '8':
                user.genrate_login()
                curseur.execute('UPDATE users SET login = ? WHERE login = ?', (user.get_login(), login))
            else:
                print('Choix invalide')
            break
    connexion.commit()
    if not user_trouve:
        print('Utilisateur non trouvé')
    return False

def delete_user():
    login = input('Login de l\'utilisateur à supprimer : ')
    #essayer de supprimer l'utilisateur de la base de données
    try:

        curseur.execute('DELETE FROM users WHERE login = ?', (login,))
        connexion.commit()
        print('Utilisateur supprimé avec succès')

        connexion.close()  # Fermer la connexion après l'opération de suppression
    # dis si une erreur se produit
    except sqlite3.Error as e:
        print('Erreur lors de la suppression de l\'utilisateur :')
    return False

def list_users():
    # Récupérer les données de tous les utilisateurs de la base de données
    data = curseur.execute('SELECT * FROM users').fetchall()
    for user in data:
        print('-----------------------------------')
        print(f'Nom : {user[1]}\nPrenom : {user[2]}\nEmail : {user[3]}\nNuméro de téléphone : {user[4]}\nRôle : {user[5]}\nDroit : {user[6]}\nLogin : {user[7]}\n')

    return False
