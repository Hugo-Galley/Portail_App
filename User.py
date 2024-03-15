# ce fichier contient les classes User et Scientifique

# Importation des modules
import string
import datetime
import secrets
from tkinter import messagebox
# Définition de la classe User
class User:
    # Constructeur de la classe User
    def __init__(self,nom,prenom,email,num_tel,role,region,unite,login = '',password = ''):
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self.__num_tel = num_tel
        self.__password = login
        self.__login = password
        self.__admin = False
        self.__role = role
        self.__region = region
        self.__unite = unite

    # Méthode pour générer un mot de passe en utilisant la librairie secrets et la librairie string

    def generate_password(self,size):
        caracter = string.ascii_letters + string.digits + string.punctuation
        for i in range(int(size)):
            self.__password += secrets.choice(caracter)
        return self.__password
    # Méthode pour générer un login en utilisant le nom et le prénom de l'utilisateur*

    def genrate_login(self):
        self.__login = self.__prenom[0] + self.__nom
        return self.__login
    # Méthode pour récupérer les attributs privés de la classe User avec utilisation de @property pour les rendre accessibles
    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @property
    def num_tel(self):
        return self.__num_tel

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def admin(self):
        return self.__admin

    @property
    def role(self):
        return self.__role

    @property
    def region(self):
        return self.__region
    @property
    def unite(self):
        return self.__unite

    # Méthode pour modifier les attributs privés de la classe User

    def set_admin(self,admin):
        self.__admin = admin

    def set_login(self,login):
        self.__login = login
    def set_password(self,password):
        self.__password = password
    def set_email(self,email):
        self.__email = email
    def set_num_tel(self,num_tel):
        self.__num_tel = num_tel
    def set_nom(self,nom):
        self.__nom = nom
    def set_prenom(self,prenom):
        self.__prenom = prenom

    def set_role(self,role):
        self.__role = role
    def set_region(self,region):
        self.__region = region
    def set_unite(self,unite):
        self.__unite = unite

# Définition de la classe Scientifique qui hérite de la classe User
class Scientifique(User):

    # Constructeur de la classe Scientifique
    def __init__(self, nom, prenom, email, num_tel, role,unite,region, numero, code_projet, date_prise_fonction, login='', password=''):
        super().__init__(nom, prenom, email, num_tel, role,unite,region, login, password)
        self.__numero = numero
        self.__code_projet = code_projet
        self.__date_prise_fonction = date_prise_fonction
        self.__responsable = False
        self.__unite = []
        self.__date_prise_fonction_responsable = ''

    def verifier_responsable(self):
        # Ajoutez ici votre logique pour vérifier si le scientifique est responsable
        # Vous pouvez comparer la date de prise de fonction avec une date de référence
        pass

    def savoir_responsable(self):
        if datetime.datetime.now().year - int(self.__date_prise_fonction) > 10:
            self.__responsable = True
            return True

    # Méthode pour récupérer les attributs privés de la classe Scientifique avec utilisation de @property pour les rendre accessibles
    @property
    def numero(self):
        return self.__numero

    @property
    def code_projet(self):
        return self.__code_projet

    @property
    def date_prise_fonction(self):
        return self.__date_prise_fonction

    @property
    def responsable(self):
        return self.__responsable

    @property
    def unite(self):
        return self.__unite

    @property
    def date_prise_fonction_responsbale(self):
        return self.__date_prise_fonction_responsbale

    # Méthode pour modifier les attributs privés de la classe Scientifique

    def set_numero(self, numero):
        self.__numero = numero

    def set_code_projet(self, code_projet):
        self.__code_projet = code_projet

    def set_date_prise_fonction(self, date_prise_fonction):
        self.__date_prise_fonction = date_prise_fonction

    # veririfer si le scientifique est responsable
    def set_responsable(self, responsable):
        # si la date de prise de fonction est supérieur à 10 ans alors le scientifique est responsable
        if datetime.datetime.now().year - self.__date_prise_fonction:
            self.__responsable = True
        self.__responsable = responsable

    def set_unite(self, unite):
        self.__unite.append(unite)



