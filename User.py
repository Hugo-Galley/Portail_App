# ce fichier contient les classes User et Scientifique

# Importation des modules
import string
import datetime
import secrets
# Définition de la classe User
class User:
    # Constructeur de la classe User
    def __init__(self,nom,prenom,email,num_tel,role,droit,login = '',password = ''):
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self.__num_tel = num_tel
        self.__password = login
        self.__login = password
        self.__admin = False
        self.__role = role
        self.droit = droit

    # Méthode pour générer un mot de passe en utilisant la librairie secrets et la librairie string
    def generate_password(self,size):
        caracter = string.ascii_letters + string.digits + string.punctuation
        for i in range(size):
            self.__password += secrets.choice(caracter)
        return self.__password
    # Méthode pour générer un login en utilisant le nom et le prénom de l'utilisateur
    def genrate_login(self):
        self.__login = self.__prenom[0] + self.__nom
        return self.__login
    # Méthode pour récupérer les attributs privés de la classe User
    def get_login(self):
        return self.__login
    def get_password(self):
        return self.__password
    def get_email(self):
        return self.__email
    def get_num_tel(self):
        return self.__num_tel
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_admin(self):
        return self.__admin
    def get_role(self):
        return self.__role
    def get_droit(self):
        return self.droit

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
        if nom == '':
            print('Le nom ne doit pas être vide')
        else:
            self.__nom = nom
    def set_prenom(self,prenom):
        self.__prenom = prenom

    def set_role(self,role):
        self.__role = role
    def set_droit(self,droit):
        self.droit = droit

# Définition de la classe Scientifique
class Scientifique(User):

    # Constructeur de la classe Scientifique
    def __init__(self,nom,prenom,email,num_tel,numero,code_projet,date_prise_fonction):
        super.__init__(nom,prenom,email,num_tel)
        self.__numero = numero
        self.__code_projet = code_projet
        self.__date_prise_fonction = date_prise_fonction
        self.__responsable = False
        self.__unite = []
        self.__date_prise_fonction_responsbale = ''
        # Méthode pour vérifier si le scientifique est responsable  en fonction de la date de prise de fonction
        def savoir_responsable(self):
            if 2024 - self.__date_prise_fonction > 10:
                self.__responsable = True

        # Méthode pour récupérer les attributs privés de la classe Scientifique
        def get_numero(self):
            return self.__numero
        def get_code_projet(self):
            return self.__code_projet
        def get_date_prise_fonction(self):
            return self.__date_prise_fonction
        def get_responsable(self):
            return self.__responsable
        def get_unite(self):
            return self.__unite
        def get_date_prise_fonction_responsbale(self):
            return self.__date_prise_fonction_responsbale

        # Méthode pour modifier les attributs privés de la classe Scientifique

        def set_numero(self,numero):
            self.__numero = numero
        def set_code_projet(self,code_projet):
            self.__code_projet = code_projet
        def set_date_prise_fonction(self,date_prise_fonction):
            self.__date_prise_fonction = date_prise_fonction
        def set_responsable(self,responsable): #veririfer si le scientifique est responsable
            if datetime.datetime.now().year - self.__date_prise_fonction:
                self.__responsable = True
            self.__responsable = responsable
        def set_unite(self,unite):
            self.__unite.append(unite)





