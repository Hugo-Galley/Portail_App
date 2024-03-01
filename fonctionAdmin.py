liste_user = []
from User import *
def add_user():
    print('Ajout d\'un utilisateur')
    user = User(input('Nom : '),input('Prenom : '),input('Email : '),input('Numéro de téléphone : '),input('Role : '),input('Droit : '))
    user.genrate_login()
    user.generate_password(8)
    liste_user.append(user)
    print('Utilisateur ajouté avec succès')

def update_user():
    login = input('Login de l\'utilisateur à modifier : ')
    choix = input('1. Modifier le nom\n2. Modifier le prénom\n3. Modifier l\'email\n4. Modifier le numéro de téléphone\n5. Modifier le rôle\n6. Modifier le droit\n7. Modifier le mot de passe\n8. Modifier le login\nVotre choix : ')
    for user in liste_user:
        if user.get_login() == login:
            if choix == '1':
                user.set_nom(input('Nouveau nom : '))
            elif choix == '2':
                user.set_prenom(input('Nouveau prénom : '))
            elif choix == '3':
                user.set_email(input('Nouvel email : '))
            elif choix == '4':
                user.set_num_tel(input('Nouveau numéro de téléphone : '))
            elif choix == '5':
                user.set_role(input('Nouveau rôle : '))
            elif choix == '6':
                user.droit = input('Nouveau droit : ')
            elif choix == '7':
                user.generate_password(8)
            elif choix == '8':
                user.genrate_login()
            else:
                print('Choix invalide')
            return

    print('Utilisateur non trouvé')

def delete_user():
    login = input('Login de l\'utilisateur à supprimer : ')
    for user in liste_user:
        if user.get_login() == login:
            liste_user.remove(user)
            print('Utilisateur supprimé avec succès')
            return
    print('Utilisateur non trouvé')

def list_users():
    for user in liste_user:
        if user in liste_user:
            print(user.get_nom())
        else :
            print('Il n y\'a aucun utilisateurs pour le moment')
            return False

