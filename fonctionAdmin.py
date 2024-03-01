from User import *
import hashlib
import sqlite3
connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()
liste_user = []
def add_user():
    print('Ajout d\'un utilisateur')
    user = User(input('Nom : '),input('Prenom : '),input('Email : '),input('Numéro de téléphone : '),input('Role : '),input('Droit : '))
    user.genrate_login()
    user.generate_password(8)
    curseur.execute('INSERT INTO users (nom, prenom, email, num_tel, role, droit,login, password) VALUES (?,?,?,?,?,?,?,?)', (user.get_nom(), user.get_prenom(), user.get_email(), user.get_num_tel(), user.get_role(), user.get_droit(), user.get_login(), hashlib.sha256(user.get_password().encode()).hexdigest()))
    connexion.commit()
    with open('bdd.txt','a') as file:
        file.write(user.get_nom() + ' ' + user.get_prenom() + ' ' + user.get_email() + ' ' + user.get_num_tel() + ' ' + user.get_role() + ' ' + user.droit + ' ' + user.get_login() + ' ' + hashlib.sha256(user.get_password().encode()).hexdigest() + '\n')
    print('Utilisateur ajouté avec succès')

def update_user():
    login = input('Login de l\'utilisateur à modifier : ')

    data = curseur.execute('SELECT * FROM users WHERE login = ?', (login,)).fetchall()
    user_trouve = False
    for user_data in data:
        if user_data[7] == login:
            user_trouve = True
            # Instancier un nouvel objet User avec les données récupérées de la base de données
            user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6])
            choix = input('1. Modifier le nom\n2. Modifier le prénom\n3. Modifier l\'email\n4. Modifier le numéro de téléphone\n5. Modifier le rôle\n6. Modifier le droit\n7. Modifier le mot de passe\n8. Modifier le login\nVotre choix : ')
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
                user.droit = input('Nouveau droit : ')
                curseur.execute('UPDATE users SET droit = ? WHERE login = ?', (user.droit, login))
            elif choix == '7':
                user.generate_password(8)
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

def delete_user():
    login = input('Login de l\'utilisateur à supprimer : ')
    try:

        curseur.execute('DELETE FROM users WHERE login = ?', (login,))
        connexion.commit()
        print('Utilisateur supprimé avec succès')

        connexion.close()  # Fermer la connexion après l'opération de suppression
    except sqlite3.Error as e:
        print('Erreur lors de la suppression de l\'utilisateur :')

def list_users():
    data = curseur.execute('SELECT * FROM users').fetchall()
    for user in data:
        print('-----------------------------------')
        print(f'Nom : {user[1]}\nPrenom : {user[2]}\nEmail : {user[3]}\nNuméro de téléphone : {user[4]}\nRôle : {user[5]}\nDroit : {user[6]}\nLogin : {user[7]}\n')


    return False
connexion.close()