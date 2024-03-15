# Description: Ce fichier contient les fonctions pour l'interface graphique du programme
# importation des modules
import hashlib
from User import *
import customtkinter as ctk
from tkinter import messagebox, YES
import sqlite3

# Connexion à la base de données
connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()
# Récupération des logins et mots de passe pour l'administrateur
loguser = curseur.execute('SELECT login FROM users WHERE role != "admin"').fetchall()
mdpuser = curseur.execute('SELECT password FROM users WHERE role != "admin"').fetchall()
# Récupération des logins et mots de passe pour les users
loginadmin = curseur.execute('SELECT login FROM users WHERE role = "admin"').fetchall()
mdpadmin = curseur.execute('SELECT password FROM users WHERE role = "admin"').fetchall()
# Récupération des logins et mots de passe pour les scientifiques
logscientifique = curseur.execute('SELECT login FROM scientifique').fetchall()
mdpscientifique = curseur.execute('SELECT password FROM scientifique').fetchall()

# Création de la fenêtre principale et attribution de ses caractéristiques
windows = ctk.CTk()
windows.title("SNT LABO")
windows.geometry("500x400")
windows.grid_rowconfigure(0, weight=1)
windows.grid_columnconfigure(0, weight=1)
scrollable_frame = ctk.CTkScrollableFrame(windows, width=200, height=200)

# Création des frames
# création de la frame pour scroll dans la fenêtre principale
fram_scroll = ctk.CTkScrollableFrame(windows, fg_color="transparent")
frame_authentication = ctk.CTkFrame(windows, fg_color="transparent")
frame_science = ctk.CTkFrame(windows, fg_color="transparent")
frame_doc_medecin = ctk.CTkFrame(windows, fg_color="transparent")
frame_doc_commercial = ctk.CTkFrame(windows, fg_color="transparent")
frame_doc_collaborateur = ctk.CTkFrame(windows, fg_color="transparent")


# Fonction de connexion
def connexion_user():
    global entre_login
    global entre_mdp
    # definition de la taille de la fenetre
    windows.geometry("500x400")

    def verif():
        cpt_tentative = 0
        # Essayer de se connecter à la base de données
        try:
            liste_user = []
            liste_mdp = []
            # Récupération des logins et mots de passe pour les users
            if loguser and mdpuser:
                for logine, mdp in zip(loguser, mdpuser):
                    liste_user.append(logine)
                    liste_mdp.append(mdp)
            # hacshage du mot de passe
            hashed_password = hashlib.sha256(entre_mdp.get().encode()).hexdigest()
            # Vérification des identifiants pour l'administrateur
            if entre_login.get() == loginadmin[0][0] and hashed_password == mdpadmin[0][0]:
                frame_authentication.pack_forget()
                mainframe()
            # Vérification des identifiants pour les scientifiques
            elif entre_login.get() in [log[0] for log in logscientifique] and hashed_password in [mdp[0] for mdp in mdpscientifique]:
                frame_authentication.pack_forget()
                document_scientifique(entre_login.get())
            # Vérification des identifiants pour les users
            elif entre_login.get() in [log[0] for log in loguser] and hashed_password in [mdp[0] for mdp in mdpuser]:
                frame_authentication.pack_forget()
                affichage_document(entre_login.get())
            # Affichage d'un message d'erreur si les identifiants sont incorrects
            else:
                messagebox.showerror("Erreur", "Login ou mot de passe incorrect")
                cpt_tentative += 1
                if cpt_tentative == 3:
                    messagebox.showerror("Erreur", "Nombre de tentative dépassé")
                    windows.destroy()
        # En cas d'erreur, afficher un message d'erreur
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s est produite : {e}")

    def toggle_show_password():
        if show_password.get():
            entre_mdp.configure(show="")
        else:
            entre_mdp.configure(show="*")

    # Creation des labels
    label_nom = ctk.CTkLabel(frame_authentication, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady=40)

    label_nom = ctk.CTkLabel(frame_authentication, text="Veuillez entrer vos identifiants de connexion",
                             fg_color="transparent", font=("Arial", 20))
    label_nom.pack(padx=10, pady=10)

    # Créer les champs de saisie
    entre_login = ctk.CTkEntry(frame_authentication, fg_color="transparent", font=("Arial", 20), width=300,
                               placeholder_text='Login')
    entre_login.pack()

    # Créer le champ de mot de passe avec l'option 'show' configurée pour masquer le texte
    entre_mdp = ctk.CTkEntry(frame_authentication, fg_color="transparent", font=("Arial", 20), width=300,
                             placeholder_text='Mot de passe', show="*")
    entre_mdp.pack(pady=10)

    # Créer la case à cocher pour afficher/masquer le mot de passe
    show_password = ctk.BooleanVar()
    show_password_checkbox = ctk.CTkCheckBox(frame_authentication, text="Afficher le mot de passe",
                                             variable=show_password,
                                             onvalue=True, offvalue=False, command=toggle_show_password)
    show_password_checkbox.pack(pady=5)

    # Créer le bouton de connexion
    btn_connexion = ctk.CTkButton(frame_authentication, text="Connexion", fg_color="grey", font=("Arial", 20),
                                  command=verif, width=300)
    btn_connexion.pack(pady=10)
    # Empaquetage de la frame
    frame_authentication.pack(fill='both', expand=True)


def mainframe():
    # Creation des frames de maniere global pour les utiliser dans les autres fonctions
    global frame_btn_choix, frame_ajouter, frame_modif_user, frame_suppr_user, frame_list_user, frame_ajout_user, frame_suppr_user
    frame_ajout_user = ctk.CTkFrame(fram_scroll, fg_color="transparent")
    frame_ajouter = ctk.CTkFrame(fram_scroll, fg_color="transparent")
    frame_modif_user = ctk.CTkFrame(windows, fg_color="transparent")
    frame_list_user = ctk.CTkFrame(fram_scroll, fg_color="transparent")
    frame_suppr_user = ctk.CTkFrame(windows, fg_color="transparent")
    frame_btn_choix = ctk.CTkFrame(windows, fg_color="transparent")

    # creation des fonctions pour les boutons
    def retour():
        frame_btn_choix.pack_forget()
        frame_authentication.pack()
        entre_login.delete(0, 'end')
        entre_mdp.delete(0, 'end')

    def ajouter():
        frame_btn_choix.pack_forget()
        frame_ajout_user.pack_forget()
        ajout_user()

    def modifier():
        frame_btn_choix.pack_forget()
        frame_modif_user.pack_forget()
        modif_user()

    def supprimmer():
        frame_btn_choix.pack_forget()
        frame_suppr_user.pack_forget()
        suppr_user()

    def lister():
        frame_btn_choix.pack_forget()
        frame_list_user.pack_forget()
        list_user()

    windows.geometry("600x500")
    # Creation des labels
    label_nom = ctk.CTkLabel(frame_btn_choix, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.grid(row=0, column=0, columnspan=2, pady=40)
    # Creation des boutons
    btn_ajout_user = ctk.CTkButton(frame_btn_choix, text="Ajouter un utilisateur", fg_color="transparent",
                                   font=("Arial", 20), command=ajouter)
    btn_ajout_user.grid(row=1, column=0, padx=10, pady=10)

    btn_modif_user = ctk.CTkButton(frame_btn_choix, text="Modifier un utilisateur", fg_color="transparent",
                                   font=("Arial", 20), command=modifier)
    btn_modif_user.grid(row=1, column=1, padx=10, pady=10)

    btn_suppr_user = ctk.CTkButton(frame_btn_choix, text="Supprimer un utilisateur", fg_color="transparent",
                                   font=("Arial", 20), command=supprimmer)
    btn_suppr_user.grid(row=2, column=0, padx=10, pady=10)

    btn_list_user = ctk.CTkButton(frame_btn_choix, text="Lister les utilisateurs", fg_color="transparent",
                                  font=("Arial", 20), command=lister)
    btn_list_user.grid(row=2, column=1, padx=10, pady=10)

    btn_quit = ctk.CTkButton(frame_btn_choix, text="Quitter", fg_color="transparent", font=("Arial", 20),
                             command=retour)
    btn_quit.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    # Empaquetage de la frame
    frame_btn_choix.pack(expand=YES)


def ajout_user():

    def ajouter_user():
        try:
            # Vérification des champs obligatoires pour l'utilisateur de base
            if enter_nom.get() == "" or enter_prenom.get() == "" or enter_email.get() == "" or enter_num_tel.get() == "" or entere_role.get() == "":
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
                return

            # Vérification des champs supplémentaires pour le scientifique
            if switch_var.get():
                # Vérification des champs obligatoires pour le scientifique
                if entere_numero.get() == "" or enter_date_prise_fonction.get() == "" or enter_code_projet.get() == "":
                    messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
                    return
                # Creation de l'objet scientifique
                user = Scientifique(enter_nom.get(), enter_prenom.get(), enter_email.get(), enter_num_tel.get(),
                                    entere_role.get(), enter_region.get(), enter_unite.get(),
                                    entere_numero.get(), enter_code_projet.get(), enter_date_prise_fonction.get())
                # Génération du login et du mot de passe
                user.genrate_login()
                user.generate_password(enter_size.get())
                # Insertion de l'utilisateur dans la base de données
                curseur.execute(
                    'INSERT INTO scientifique (nom, prenom, email, num_tel, role, region, unite, numero, code_projet, date_prise_foncion, login, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)',
                    (user.nom, user.prenom, user.email, user.num_tel, user.role, user.region, user.unite, user.numero,
                     user.code_projet, user.date_prise_fonction, user.login,
                     hashlib.sha256(user.password.encode()).hexdigest()))
            else:
                # Creation de l'objet user
                user = User(enter_nom.get(), enter_prenom.get(), enter_email.get(), enter_num_tel.get(),
                            entere_role.get(), enter_region.get(), enter_unite.get())
                user.genrate_login()
                user.generate_password(enter_size.get())
                # Insertion de l'utilisateur dans la base de données
                curseur.execute(
                    'INSERT INTO users (nom, prenom, email, num_tel, role, region, unite, login, password) VALUES (?,?,?,?,?,?,?,?,?)',
                    (user.nom, user.prenom, user.email, user.num_tel, user.role, user.region, user.unite,
                     user.login, hashlib.sha256(user.password.encode()).hexdigest()))

            # Vérification du role
            while True:
                role = entere_role.get()
                # si le droit n'est pas correct, afficher un message d'erreur
                if role not in ['Medecin', 'Commerciale', 'Autres', 'Scientifique']:
                    messagebox.showerror("Erreur", "Role incorrect, veuillez réessayer.")
                    return
                else:
                    break

            connexion.commit()

            # Affichage d'un message de succès
            messagebox.showinfo("Succès",
                                f"Utilisateur ajouté avec succès\nLogin : {user.login}\nMot de passe : {user.password}")

        except sqlite3.Error as e:
            # En cas d'erreur, afficher un message d'erreur
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

        # Fonction pour l'affichage des champs supplémentaires pour le scientifique

    def affichage_scientifique():
        # Si le bouton est activé, afficher les champs supplémentaires
        if combobox_calllback_mdp() == "Scientifique":
            entere_numero.pack(pady=10)
            label_prise_fonction.pack(pady=10)
            enter_date_prise_fonction.pack(pady=10)
            enter_code_projet.pack(pady=10)
        # Sinon, les cacher
        else:
            entere_numero.pack_forget()
            enter_date_prise_fonction.pack_forget()
            enter_code_projet.pack_forget()
            label_prise_fonction.pack_forget()

    # Fonction pour l'affichage des champs supplémentaires pour le scientifique
    def affichage_scientifiquee():
        # Si le bouton est activé, afficher les champs supplémentaires
        if switch_var.get() == True:
            entere_numero.pack(pady=10)
            label_prise_fonction.pack(pady=10)
            enter_date_prise_fonction.pack(pady=10)
            enter_code_projet.pack(pady=10)
        # Sinon, les cacher
        else:
            entere_numero.pack_forget()
            enter_date_prise_fonction.pack_forget()
            enter_code_projet.pack_forget()
            label_prise_fonction.pack_forget()

    choix_anne = 2024

    # Recuperation de l'année choisie
    def combobox_calllback(choice):
        choix_anne = choice
    def combobox_calllback_mdp(choice):
        choix_mdp = choice

    # Recuperation du role choisi
    def combobox_calllback_role(choice):
        choix_role = choice

    def retour():
        frame_ajout_user.pack_forget()
        frame_ajouter.pack_forget()
        fram_scroll.pack_forget()
        mainframe()

    # Creation des variables
    switch_var = ctk.BooleanVar(value=False)
    switch_var_medecin = ctk.BooleanVar(value=False)

    windows.geometry("600x900")
    # Creation des labels
    label_nom = ctk.CTkLabel(frame_ajout_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady=40)

    label_nom = ctk.CTkLabel(frame_ajout_user, text="Ajouter un utilisateur", fg_color="transparent",
                             font=("Arial", 20))
    label_nom.pack(padx=10, pady=10)
    # Creation des champs de saisie
    enter_nom = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                             placeholder_text='Nom')
    enter_nom.pack(pady=10)

    enter_prenom = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                                placeholder_text='Prenom')
    enter_prenom.pack(pady=10)

    enter_email = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                               placeholder_text='Email')
    enter_email.pack(pady=10)

    enter_num_tel = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                                 placeholder_text='Numero de telephone')
    enter_num_tel.pack(pady=10)

    ctk.CTkLabel(frame_ajout_user, text="Role", fg_color="transparent", font=("Arial", 20)).pack()

    entere_role = ctk.CTkComboBox(frame_ajout_user, values=['Medecin', 'Commerciale','Scientifique', 'Autres'],
                                  command=combobox_calllback_role)
    entere_role.pack(pady=10)
    ctk.CTkLabel(frame_ajout_user, text="Taille MDP", fg_color="transparent", font=("Arial", 20)).pack()
    enter_size = ctk.CTkComboBox(frame_ajout_user, values=['8', '10', '12', '14', '16', '18', '20', '22', '24', '26'],command=combobox_calllback_mdp)
    enter_size.pack(pady=10)

    enter_region = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                                placeholder_text='Region')
    enter_region.pack(pady=10)

    enter_unite = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                               placeholder_text='Unite')
    enter_unite.pack(pady=10)

    # Creation du bouton pour activer ou désactiver les champs supplémentaires pour le scientifique
    ctk.CTkSwitch(frame_ajout_user, text="Scientifique", variable=switch_var, onvalue=True,
                  offvalue=False, command=affichage_scientifiquee).pack()

    entere_numero = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                                 placeholder_text='Numero de labo')
    label_prise_fonction = ctk.CTkLabel(frame_ajout_user, text="Date de prise de fonction", fg_color="transparent",
                                        font=("Arial", 20))
    # Creation de la liste déroulante pour l'année de prise de fonction
    liste_anne = ['2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013',
                  '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001',
                  '2000', '1999', '1998', '1997']
    enter_date_prise_fonction = ctk.CTkComboBox(frame_ajout_user, values=liste_anne, command=combobox_calllback)

    enter_code_projet = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                                     placeholder_text='Code du projet')

    ctk.CTkButton(frame_ajouter, text="Ajouter", fg_color="grey", font=("Arial", 20), command=ajouter_user,
                  width=300).pack()

    ctk.CTkButton(frame_ajouter, text="Quitter", fg_color="grey", font=("Arial", 20), command=retour).pack(pady=10)

    # Empaquetage des frames
    frame_ajout_user.pack(pady=50, expand=YES)
    frame_ajouter.pack(expand=YES)
    fram_scroll.pack(fill='both', expand=True)


def modif_user():
    def modifier_user():
        try:
            # Recuperation des données de l'utilisateur
            data = curseur.execute('SELECT * FROM users WHERE login = ?', (enter_nom.get(),)).fetchall()
            data2 = curseur.execute('SELECT * FROM scientifique WHERE login = ?', (enter_nom.get(),)).fetchall()
            user_trouve = False
            # Verification de l'existence de l'utilisateur
            for user_data in data or data2:
                # Si l'utilisateur est trouvé, création de l'objet user
                if user_data[9] == enter_nom.get():

                    user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5],
                                user_data[6], user_data[7], user_data[8])
                    user_trouve = True
                    # Modification des données de l'utilisateur
                    if option_menu.get() == "Nom":
                        user.set_nom(enter_modif.get())
                        curseur.execute('UPDATE users SET nom = ? WHERE login = ?', (user.nom, enter_nom.get()))
                    if option_menu.get() == "Prenom":
                        user.set_prenom(enter_modif.get())
                        curseur.execute('UPDATE users SET prenom = ? WHERE login = ?', (user.prenom, enter_nom.get()))
                    if option_menu.get() == "Email":
                        user.set_email(enter_modif.get())
                        curseur.execute('UPDATE users SET email = ? WHERE login = ?', (user.email, enter_nom.get()))
                    if option_menu.get() == "Numero de telephone":
                        user.set_num_tel(enter_modif.get())
                        curseur.execute('UPDATE users SET num_tel = ? WHERE login = ?', (user.num_tel, enter_nom.get()))
                    if option_menu.get() == "Role":
                        # Verification du droit
                        if enter_modif.get() not in ['md', 'cm', 'etc', 'sc']:
                            messagebox.showerror("Erreur", "Role incorrect")
                        else:
                            user.set_role(enter_modif.get())
                            curseur.execute('UPDATE users SET role = ? WHERE login = ?', (user.role, enter_nom.get()))

                    connexion.commit()
            # Si l'utilisateur n'est pas trouvé, afficher un message d'erreur
            if not user_trouve:
                messagebox.showerror("Erreur", "Utilisateur non trouvé")
                frame_modif_user.pack_forget()
                mainframe()
            # Sinon, afficher un message de succès et effacer les frames
            else:
                messagebox.showinfo("Succès", "Utilisateur modifié avec succès")
                frame_modif_user.pack_forget()
                frame_btn_choix.pack()

        # En cas d'erreur, afficher un message d'erreur et effacer les frames
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
            frame_modif_user.pack_forget()
            frame_btn_choix.pack()

    def retour():
        frame_modif_user.pack_forget()
        frame_btn_choix.pack()

    # Creation des labels
    label_nom = ctk.CTkLabel(frame_modif_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady=40)
    # Creation des champs de saisie
    enter_nom = ctk.CTkEntry(frame_modif_user, fg_color="transparent", font=("Arial", 20), width=300,
                             placeholder_text='login')
    enter_nom.pack(pady=10)
    # Creation de la liste déroulante pour les années
    options = ["Nom", "Prenom", "Email", "Numero de telephone", "Role"]
    option_menu = ctk.CTkOptionMenu(frame_modif_user, values=options)
    option_menu.pack(pady=10)

    enter_modif = ctk.CTkEntry(frame_modif_user, fg_color="transparent", font=("Arial", 20), width=300,
                               placeholder_text='Nouvelle Valeur')
    enter_modif.pack(pady=10)
    # Creation du bouton pour modifier l'utilisateur
    btn_connexion = ctk.CTkButton(frame_modif_user, text="Modifier", fg_color="grey", font=("Arial", 20),
                                  command=modifier_user, width=300)
    btn_connexion.pack(pady=10)
    # Creation du bouton pour quitter
    ctk.CTkButton(frame_modif_user, text="Quitter", fg_color="grey", font=("Arial", 20), command=retour).pack(pady=10)
    # Empaquetage de la frame
    frame_modif_user.pack(pady=40)


def suppr_user():
    def supprimer_user():
        try:
            # Verification si le champ est vide
            while True:
                login = enter_nom.get()
                if login == "":
                    messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
                    return
                else:
                    break
            # Verification de l'existence de l'utilisateur
            while True:
                if enter_nom.get() not in [log[0] for log in loguser]:
                    messagebox.showinfo("Erreur", "Login incorrect")

                    return
                else:
                    messagebox.showerror(title="Reussite", message="Utilisateur supprimé avec succès")
                    break

            frame_suppr_user.pack_forget()
            mainframe()
        # En cas d'erreur, afficher un message d'erreur et effacer les frames
        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
            frame_suppr_user.pack_forget()
            mainframe()

    def retour():
        frame_suppr_user.pack_forget()
        mainframe()

    # Création des labels
    label_nom = ctk.CTkLabel(frame_suppr_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady=40)
    # Création des champs de saisie
    enter_nom = ctk.CTkEntry(frame_suppr_user, fg_color="transparent", font=("Arial", 20), width=300,
                             placeholder_text='login')
    enter_nom.pack(pady=10)
    # Création du bouton pour supprimer l'utilisateur
    btn_supprimer = ctk.CTkButton(frame_suppr_user, text="Supprimer", fg_color="grey", font=("Arial", 20),
                                  command=supprimer_user, width=300)
    btn_supprimer.pack(pady=10)
    # Création du bouton pour quitter
    ctk.CTkButton(frame_suppr_user, text="Quitter", fg_color="grey", font=("Arial", 20), command=retour).pack(pady=10)
    # Empaquetage de la frame
    frame_suppr_user.pack(expand=YES)


def list_user():
    def quitter():
        frame_list_user.pack_forget()
        fram_scroll.pack_forget()
        mainframe()

    # Recuperation des données de la base de données
    data = curseur.execute('SELECT * FROM users').fetchall()
    # Affichage des utilisateurs dans le cadre
    Logo = ctk.CTkLabel(frame_list_user, text="Liste des utilisateurs", fg_color="transparent", font=("Arial", 40))
    Logo.pack(pady=40)
    for user in data:
        label_nom = ctk.CTkLabel(frame_list_user,
                                 text=f'Nom : {user[1]} Prenom : {user[2]} Email : {user[3]} Numéro de téléphone : {user[4]} Rôle : {user[5]} Unite : {user[7]} Login : {user[9]}',
                                 fg_color="transparent", font=("Arial", 20))
        ctk.CTkLabel(frame_list_user, text="---------------------------------------------", fg_color="transparent",
                     font=("Arial", 12)).pack()
        label_nom.pack(padx=10, pady=10)

    # Ajout d'un bouton "Retour"
    ctk.CTkButton(frame_list_user, text="Retour", fg_color="grey", font=("Arial", 20), command=quitter).pack(pady=10)

    frame_list_user.pack(expand=YES)
    fram_scroll.pack(fill='both', expand=True)


def document_scientifique(log):
    global user

    def retour():
        frame_science.pack_forget()
        connexion_user()

    # Recuperation des données de la base de données
    data = curseur.execute('SELECT * FROM scientifique WHERE login = ?', (log,)).fetchall()
    for info in data:
        # Creation de l'objet scientifique
        user = Scientifique(info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10],
                            info[11])
    # Verification si l'utilisateur est responsable
    if user.savoir_responsable():
        ctk.CTkLabel(frame_science, text="Vous êtes responsable", fg_color="transparent", font=("Arial", 20)).pack()

    # Creation des labels
    label_nom = ctk.CTkLabel(frame_science, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()
    ctk.CTkLabel(frame_science, text="---------------------------------------------", fg_color="transparent",
                 font=("Arial", 20)).pack()
    label_nom = ctk.CTkLabel(frame_science, text="Bienvenue sur l'interface scientifique", fg_color="transparent",
                             font=("Arial", 20))
    label_nom.pack(padx=10, pady=10)
    ctk.CTkLabel(frame_science, text="---------------------------------------------", fg_color="transparent",
                 font=("Arial", 20)).pack()
    # Creation des boutons
    ctk.CTkButton(frame_science, text="Quitter", fg_color="grey", font=("Arial", 20), command=retour).pack(pady=10)
    # Empaquetage de la frame
    frame_science.pack(expand=YES)


def affichage_document(log):
    global user
    # Recuperation des données de la base de données
    data = curseur.execute('SELECT * FROM users WHERE login = ?', (log,)).fetchall()
    for info in data:
        # Creation de l'objet user
        user = User(info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])
    # Verification du droit pour l'affichage des documents
    if user.role == 'Medecin':
        affichage_doc_medecin()
    elif user.role == 'Commerciale':
        affichage_doc_commericale()
    elif user.role == 'Autres':
        affichage_doc_collaborateur()
    else:
        messagebox.showerror('Erreur', 'Erreur de role')


def affichage_doc_medecin():
    def retour():
        frame_doc_medecin.pack_forget()
        connexion_user()

    windows.title('Espace Medecin')
    # Creation des labels
    titre = ctk.CTkLabel(frame_doc_medecin, text='Espace Medecin', font=('Arial', 30)).pack(pady=20)

    ctk.CTkLabel(frame_doc_medecin, text='Document 1', font=('Arial', 20)).pack(pady=10)
    ctk.CTkLabel(frame_doc_medecin, text='Document 2', font=('Arial', 20)).pack(pady=10)
    ctk.CTkLabel(frame_doc_medecin, text='Document 3', font=('Arial', 20)).pack(pady=10)
    # Creation du bouton pour quitter
    ctk.CTkButton(frame_doc_medecin, text='Quitter', font=('Arial', 20), command=retour).pack(pady=10)
    # Empaquetage de la frame
    frame_doc_medecin.pack(expand=YES)


def affichage_doc_commericale():
    def retour():
        frame_doc_commercial.pack_forget()
        connexion_user()

    windows.title('Espace Commerciale')

    # Creation des labels
    titre = ctk.CTkLabel(frame_doc_commercial, text='Espace Commerciale', font=('Arial', 30)).pack(pady=20)

    ctk.CTkLabel(frame_doc_commercial, text='Document 1', font=('Arial', 20)).pack(pady=10)
    ctk.CTkLabel(frame_doc_commercial, text='Document 2', font=('Arial', 20)).pack(pady=10)
    ctk.CTkLabel(frame_doc_commercial, text='Document 3', font=('Arial', 20)).pack(pady=10)
    # Creation du bouton pour quitter
    ctk.CTkButton(frame_doc_commercial, text='Quitter', font=('Arial', 20), command=retour).pack(pady=10)
    # Empaquetage de la frame
    frame_doc_commercial.pack(expand=YES)


def affichage_doc_collaborateur():
    def retour():
        frame_doc_collaborateur.pack_forget()
        connexion_user()

    windows.title('Espace Collaborateur')

    # Creation des labels
    titre = ctk.CTkLabel(frame_doc_collaborateur, text='Espace Collaborateur', font=('Arial', 30)).pack(pady=20)

    ctk.CTkLabel(frame_doc_collaborateur, text='Document 1', font=('Arial', 20)).pack(pady=10)
    ctk.CTkLabel(frame_doc_collaborateur, text='Document 2', font=('Arial', 20)).pack(pady=10)
    ctk.CTkLabel(frame_doc_collaborateur, text='Document 3', font=('Arial', 20)).pack(pady=10)
    # Creation du bouton pour quitter
    ctk.CTkButton(frame_doc_collaborateur, text='Quitter', font=('Arial', 20), command=retour).pack(pady=10)
    # Empaquetage de la frame
    frame_doc_collaborateur.pack(expand=YES)

mainframe()
windows.mainloop()