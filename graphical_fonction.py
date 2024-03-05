import hashlib
from pickle import FALSE

from User import *
import customtkinter as ctk
from tkinter import messagebox, YES
import tkinter as tk
import sqlite3


connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()
loguser = curseur.execute('SELECT login FROM users WHERE role != "admin"').fetchall()
mdpuser = curseur.execute('SELECT password FROM users WHERE role != "admin"').fetchall()
loginadmin = curseur.execute('SELECT login FROM users WHERE role = "admin"').fetchall()
mdpadmin = curseur.execute('SELECT password FROM users WHERE role = "admin"').fetchall()
logscientifique = curseur.execute('SELECT login FROM scientifique').fetchall()
mdpscientifique = curseur.execute('SELECT password FROM scientifique').fetchall()

windows = ctk.CTk()
windows.title("SNT LABO")
windows.geometry("500x400")# Créer le widget Text

frame_authentication = ctk.CTkFrame(windows, fg_color="transparent")
frame_btn_choix = ctk.CTkFrame(windows, fg_color="transparent")
frame_ajout_user = ctk.CTkFrame(windows, fg_color="transparent")
frame_ajouter = ctk.CTkFrame(windows, fg_color="transparent")
frame_modif_user = ctk.CTkFrame(windows, fg_color="transparent")
frame_list_user = ctk.CTkFrame(windows, fg_color="transparent")
frame_suppr_user = ctk.CTkFrame(windows, fg_color="transparent")
frame_science = ctk.CTkFrame(windows, fg_color="transparent")
frame_doc_medecin = ctk.CTkFrame(windows, fg_color="transparent")
frame_doc_commercial = ctk.CTkFrame(windows, fg_color="transparent")
frame_doc_collaborateur = ctk.CTkFrame(windows, fg_color="transparent")


def connexion_user():
    windows.geometry("500x400")
    def verif():
        try:
            liste_user = []
            liste_mdp = []
            if loguser and mdpuser:
                for logine, mdp in zip(loguser, mdpuser):
                    liste_user.append(logine)
                    liste_mdp.append(mdp)

            hashed_password = hashlib.sha256(entre_mdp.get().encode()).hexdigest()
            if entre_login.get() == loginadmin[0][0] and hashed_password == mdpadmin[0][0]:
                frame_authentication.pack_forget()
                mainframe()
            elif entre_login.get() in [log[0] for log in logscientifique] and hashed_password in [mdp[0] for mdp in mdpscientifique]:
                frame_authentication.pack_forget()
                document_scientifique(entre_login.get())
            elif entre_login.get() in [log[0] for log in loguser] and hashed_password in [mdp[0] for mdp in mdpuser]:
                frame_authentication.pack_forget()
                affichage_document(entre_login.get())
            else:
                messagebox.showerror("Erreur", "Login ou mot de passe incorrect")

        except Exception as e:
            print("Erreur de connexion:", e)



    # Creation des labels
    label_nom = ctk.CTkLabel(frame_authentication, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady=40)

    label_nom = ctk.CTkLabel(frame_authentication, text="Veuillez entrer vos identifiants de connexion", fg_color="transparent", font=("Arial", 20))
    label_nom.pack(padx=10, pady=10)

    entre_login = ctk.CTkEntry(frame_authentication, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Login')
    entre_login.pack()

    entre_mdp = ctk.CTkEntry(frame_authentication, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Mot de passe')
    entre_mdp.pack(pady=10)

    btn_connexion = ctk.CTkButton(frame_authentication, text="Connexion", fg_color="grey", font=("Arial", 20), command=verif,width=300)
    btn_connexion.pack(pady=10)

    frame_authentication.pack(expand=YES)
def mainframe():
    def retour():
        frame_btn_choix.pack_forget()
        connexion_user()

    def ajouter():
        frame_btn_choix.pack_forget()
        ajout_user()

    def modifier():
        frame_btn_choix.pack_forget()
        modif_user()

    def supprimmer():
        frame_btn_choix.pack_forget()
        suppr_user()


    def lister():
        frame_btn_choix.pack_forget()
        list_user()


    windows.geometry("600x500")
    # Creation des labels
    label_nom = ctk.CTkLabel(frame_btn_choix, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.grid(row=0, column=0, columnspan=2, pady=40)

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

    frame_btn_choix.pack(expand=YES)

def ajout_user():
    def ajouter_user():
        try:
            # Vérification des champs obligatoires pour l'utilisateur de base
            if enter_nom.get() == "" or enter_prenom.get() == "" or enter_email.get() == "" or enter_num_tel.get() == "" or enter_droit.get() == "" or entere_role.get() == "":
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
                return

            # Vérification des champs supplémentaires pour le scientifique
            if switch_var.get():
                if entere_numero.get() == "" or enter_date_prise_fonction.get() == "" or enter_code_projet.get() == "":
                    messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
                    return
                user = Scientifique(enter_nom.get(), enter_prenom.get(), enter_email.get(), enter_num_tel.get(),
                                    entere_role.get(), enter_droit.get(), entere_numero.get(), enter_code_projet.get(),
                                    choix_anne)
                user.genrate_login()
                user.generate_password(8)
                curseur.execute('INSERT INTO scientifique (nom, prenom, email, num_tel, role, droit,numero,code_projet,date_prise_foncion, login, password) VALUES (?,?,?,?,?,?,?,?,?,?,?)',(user.nom(), user.prenom(), user.email(), user.num_tel(), user.role(), user.droit(), user.numero(), user.code_projet(), user.date_prise_fonction(), user.login(), hashlib.sha256(user.password().encode()).hexdigest()))
            else:
                user = User(enter_nom.get(), enter_prenom.get(), enter_email.get(), enter_num_tel.get(),
                            entere_role.get(), enter_droit.get())
                user.genrate_login()
                user.generate_password(8)
                curseur.execute(
                    'INSERT INTO users (nom, prenom, email, num_tel, role, droit, login, password) VALUES (?,?,?,?,?,?,?,?)',
                    (user.nom(), user.prenom(), user.email(), user.num_tel(), user.role(),
                     user.droit(), user.login(), hashlib.sha256(user.password().encode()).hexdigest()))



            # Vérification du droit
            while True:
                droit = enter_droit.get()
                if droit not in ['md', 'cm', 'etc','sc']:
                    messagebox.showerror("Erreur", "Droit incorrect, veuillez réessayer.")
                    return
                else:
                    break

            # Insertion de l'utilisateur dans la base de données

            connexion.commit()

            # Effacement des frames et affichage d'un message de succès
            frame_ajout_user.pack_forget()
            frame_ajouter.pack_forget()
            frame_btn_choix.pack()
            messagebox.showinfo("Succès",
                                f"Utilisateur ajouté avec succès\nLogin : {user.login()}\nMot de passe : {user.password()}")

        except sqlite3.Error as e:
            # En cas d'erreur, afficher un message d'erreur et effacer les frames
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
            frame_ajout_user.pack_forget()
            frame_ajouter.pack_forget()
            frame_btn_choix.pack()

    def affichage_scientifique():
        if switch_var.get() == True:
            entere_numero.pack(pady=10)
            label_prise_fonction.pack(pady=10)
            enter_date_prise_fonction.pack(pady=10)
            enter_code_projet.pack(pady=10)

        else:
            entere_numero.pack_forget()
            enter_date_prise_fonction.pack_forget()
            enter_code_projet.pack_forget()
            label_prise_fonction.pack_forget()
    choix_anne = 2024
    def combobox_calllback(choice):
        choix_anne = choice



    switch_var = ctk.BooleanVar(value=False)
    switch_var_medecin = ctk.BooleanVar(value=False)

    # Creation de la frame

    windows.geometry("600x900")
    # Creation des labels
    label_nom = ctk.CTkLabel(frame_ajout_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady=40)

    label_nom = ctk.CTkLabel(frame_ajout_user, text="Ajouter un utilisateur", fg_color="transparent", font=("Arial", 20))
    label_nom.pack(padx=10, pady=10)

    enter_nom = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Nom')
    enter_nom.pack(pady=10)

    enter_prenom = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Prenom')
    enter_prenom.pack(pady=10)

    enter_email = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Email')
    enter_email.pack(pady=10)

    enter_num_tel = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Numero de telephone')
    enter_num_tel.pack(pady=10)

    enter_droit = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Droit')
    enter_droit.pack(pady=10)

    entere_role = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Role')
    entere_role.pack(pady=10)

    ctk.CTkSwitch(frame_ajout_user, text="Scientifique", variable=switch_var, onvalue=True,
                                        offvalue=False, command=affichage_scientifique).pack()


    entere_numero = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                                 placeholder_text='Numero de labo')
    label_prise_fonction = ctk.CTkLabel(frame_ajout_user, text="Date de prise de fonction", fg_color="transparent", font=("Arial", 20))
    enter_date_prise_fonction = ctk.CTkComboBox(frame_ajout_user, values=['2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000', '1999', '1998', '1997'],command=combobox_calllback)

    enter_code_projet = ctk.CTkEntry(frame_ajout_user, fg_color="transparent", font=("Arial", 20), width=300,
                                     placeholder_text='Code du projet')





    ctk.CTkButton(frame_ajouter, text="Ajouter", fg_color="grey", font=("Arial", 20),command=ajouter_user,width=300).pack()

    frame_ajout_user.pack(pady=50,expand=YES)
    frame_ajouter.pack(expand=YES)

def modif_user():
    def modifier_user():
        try:
            data = curseur.execute('SELECT * FROM users WHERE login = ?', (enter_nom.get(),)).fetchall()
            data2 = curseur.execute('SELECT * FROM scientifique WHERE login = ?', (enter_nom.get(),)).fetchall()
            user_trouve = False
            for user_data in data or data2:
                if user_data[7] == enter_nom.get():
                    user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6])
                    user_trouve = True
                    if option_menu.get() == "Nom":
                        user.set_nom(enter_modif.get())
                        curseur.execute('UPDATE users SET nom = ? WHERE login = ?', (user.nom(), enter_nom.get()))
                    if option_menu.get() == "Prenom":
                        user.set_prenom(enter_modif.get())
                        curseur.execute('UPDATE users SET prenom = ? WHERE login = ?', (user.prenom(), enter_nom.get()))
                    if option_menu.get() == "Email":
                        user.set_email(enter_modif.get())
                        curseur.execute('UPDATE users SET email = ? WHERE login = ?', (user.email(), enter_nom.get()))
                    if option_menu.get() == "Numero de telephone":
                        user.set_num_tel(enter_modif.get())
                        curseur.execute('UPDATE users SET num_tel = ? WHERE login = ?', (user.num_tel(), enter_nom.get()))
                    if option_menu.get() == "Droit":
                        if enter_modif.get() not in ['md', 'cm', 'etc','sc']:
                            messagebox.showerror("Erreur", "Droit incorrect")
                        else:
                            user.set_droit(enter_modif.get())
                            curseur.execute('UPDATE users SET droit = ? WHERE login = ?', (user.droit(), enter_nom.get()))
                    if option_menu.get() == "Role":
                        user.set_role(enter_modif.get())
                        curseur.execute('UPDATE users SET role = ? WHERE login = ?', (user.role(), enter_nom.get()))
                    connexion.commit()

            if not user_trouve:
               messagebox.showerror("Erreur", "Utilisateur non trouvé")
               frame_modif_user.pack_forget()
               mainframe()
            else :
                messagebox.showinfo("Succès", "Utilisateur modifié avec succès")
                frame_modif_user.pack_forget()
                mainframe()


        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
            frame_modif_user.pack_forget()
            frame_btn_choix.pack()



    # Creation de la frame
    # Creation des labels
    label_nom = ctk.CTkLabel(frame_modif_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady=40)

    enter_nom = ctk.CTkEntry(frame_modif_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='login')
    enter_nom.pack(pady=10)

    options = ["Nom", "Prenom", "Email", "Numero de telephone", "Droit", "Role"]
    option_menu = ctk.CTkOptionMenu(frame_modif_user, values=options)
    option_menu.pack(pady=10)

    enter_modif = ctk.CTkEntry(frame_modif_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Nouvelle Valeur')
    enter_modif.pack(pady=10)

    btn_connexion = ctk.CTkButton(frame_modif_user, text="Modifier", fg_color="grey", font=("Arial", 20), command=modifier_user,width=300)
    btn_connexion.pack(pady=10)

    frame_modif_user.pack(pady=40)

def suppr_user():
    def supprimer_user():
        try:
            while True:
                login = enter_nom.get()
                if login == "":
                    messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
                    return
                else:
                    break
            while True:
                if enter_nom.get() not in [log[0] for log in loguser]:
                    messagebox.showinfo("Erreur", "Login incorrect")

                    return
                else:
                    messagebox.showerror(title="Reussite", message="Utilisateur supprimé avec succès")
                    break


            frame_suppr_user.pack_forget()
            mainframe()
        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
            frame_suppr_user.pack_forget()
            frame_btn_choix.pack()

        # Appel de mainframe() avant de détruire la fenêtre



    # Création de la frame


    # Création des labels
    label_nom = ctk.CTkLabel(windows, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady = 40)

    enter_nom = ctk.CTkEntry(frame_suppr_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='login')
    enter_nom.pack(pady=10)

    btn_supprimer = ctk.CTkButton(frame_suppr_user, text="Supprimer", fg_color="grey", font=("Arial", 20), command=supprimer_user,width=300)
    btn_supprimer.pack(pady=10)

    frame_suppr_user.pack(expand=YES)

def list_user():

    def quitter():
        frame_list_user.pack_forget()
        frame_btn_choix.pack()

    data = curseur.execute('SELECT * FROM users').fetchall()



    windows.geometry("1200x1000")
    # Creation des labels
    label_nom = ctk.CTkLabel(frame_list_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()
    for user in data:
        label_nom = ctk.CTkLabel(frame_list_user, text=f'Nom : {user[1]} Prenom : {user[2]} Email : {user[3]} Numéro de téléphone : {user[4]} Rôle : {user[5]} Droit : {user[6]} Login : {user[7]}', fg_color="transparent", font=("Arial", 20))
        ctk.CTkLabel(frame_list_user, text="---------------------------------------------", fg_color="transparent", font=("Arial", 20)).pack()
        label_nom.pack(padx=10, pady=10)

    ctk.CTkButton(frame_list_user, text="Retour", fg_color="grey", font=("Arial", 20), command=quitter).pack(pady=10)



    frame_list_user.pack(pady=50)

def document_scientifique(log):
    def retour():
        frame_science.pack_forget()
        connexion_user()
    data = curseur.execute('SELECT * FROM scientifique WHERE login = ?', (log,)).fetchall()
    for info in data:
        user = Scientifique(info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10])
    if user.savoir_responsable():
        ctk.CTkLabel(frame_science, text="Vous êtes responsable", fg_color="transparent", font=("Arial", 20)).pack()

    # Creation des labels
    label_nom = ctk.CTkLabel(frame_science, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()
    ctk.CTkLabel(frame_science, text="---------------------------------------------", fg_color="transparent", font=("Arial", 20)).pack()
    label_nom = ctk.CTkLabel(frame_science, text="Bienvenue sur l'interface scientifique", fg_color="transparent", font=("Arial", 20))
    label_nom.pack(padx=10, pady=10)
    ctk.CTkLabel(frame_science, text="---------------------------------------------", fg_color="transparent", font=("Arial", 20)).pack()
    ctk.CTkButton(frame_science, text="Quitter", fg_color="grey", font=("Arial", 20), command=retour).pack(pady=10)
    frame_science.pack(expand=YES)

def affichage_document(log):
    data = curseur.execute('SELECT * FROM users WHERE login = ?', (log,)).fetchall()
    for info in data :
        user = User(info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8])
    if user.droit() == 'md':
        affichage_doc_medecin()
    elif user.droit() == 'cm':
        affichage_doc_commericale()
    elif user.droit() == 'etc':
        affichage_doc_collaborateur()
    else:
        messagebox.showerror('Erreur', 'Erreur de role')

def affichage_doc_medecin():

    windows.title('Espace Medecin')



    titre = ctk.CTkLabel(frame_doc_medecin, text='Espace Medecin', font=('Arial', 30)).pack(pady=20)

    doc1 = ctk.CTkLabel(frame_doc_medecin, text='Document 1', font=('Arial', 20)).pack(pady=10)
    doc2 = ctk.CTkLabel(frame_doc_medecin, text='Document 2', font=('Arial', 20)).pack(pady=10)
    doc3 = ctk.CTkLabel(frame_doc_medecin, text='Document 3', font=('Arial', 20)).pack(pady=10)

    frame_doc_medecin.pack(expand=YES)

def affichage_doc_commericale():

    windows.title('Espace Commerciale')


    titre = ctk.CTkLabel(frame_doc_commercial, text='Espace Commerciale', font=('Arial', 30)).pack(pady=20)

    doc1 = ctk.CTkLabel(frame_doc_commercial, text='Document 1', font=('Arial', 20)).pack(pady=10)
    doc2 = ctk.CTkLabel(frame_doc_commercial, text='Document 2', font=('Arial', 20)).pack(pady=10)
    doc3 = ctk.CTkLabel(frame_doc_commercial, text='Document 3', font=('Arial', 20)).pack(pady=10)

    frame_doc_commercial.pack(expand=YES)
def affichage_doc_collaborateur():

    windows.title('Espace Collaborateur')


    titre = ctk.CTkLabel(frame_doc_collaborateur, text='Espace Collaborateur', font=('Arial', 30)).pack(pady=20)

    doc1 = ctk.CTkLabel(frame_doc_collaborateur, text='Document 1', font=('Arial', 20)).pack(pady=10)
    doc2 = ctk.CTkLabel(frame_doc_collaborateur, text='Document 2', font=('Arial', 20)).pack(pady=10)
    doc3 = ctk.CTkLabel(frame_doc_collaborateur, text='Document 3', font=('Arial', 20)).pack(pady=10)

    frame_doc_collaborateur.pack(expand=YES)

