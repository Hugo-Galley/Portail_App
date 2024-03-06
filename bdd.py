# Description: Création de la base de données
# importation des modules
import sqlite3
import hashlib
# Connexion à la base de données
connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()

# Création des tables
curseur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, email TEXT, num_tel TEXT, role TEXT, droit TEXT, login TEXT, password TEXT)')
curseur.execute('CREATE TABLE IF NOT EXISTS scientifique (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, email TEXT, num_tel TEXT, role TEXT, droit TEXT,numero INT,code_projet TEXT,date_prise_foncion TEXT, login TEXT, password TEXT)')
# Création de l'administrateur
admin_mdp = hashlib.sha256('admin'.encode()).hexdigest()
curseur.execute('INSERT INTO users (nom, prenom, email, num_tel, role, droit, login, password) VALUES (?,?,?,?,?,?,?,?)', ('admin', 'admin', 'test@test.com', '0606060606', 'admin', 'admin', 'admin', admin_mdp))

connexion.commit()
connexion.close()