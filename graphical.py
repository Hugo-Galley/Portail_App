import hashlib
from User import *

import customtkinter as ctk
import CTkMessagebox as ctkmsg
from tkinter import messagebox
import sqlite3
connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()


def connexion_user(login,motdepase):
    def verif():
        try:

            hashed_password = hashlib.sha256(entre_mdp.get().encode()).hexdigest()
            if entre_login.get() == login[0][0] and hashed_password == motdepase[0][0]:
                ctkmsg.CTkMessagebox(message="Connexion Réussie", icon="check", option_1="Merci")
                mainframe()
            else:
                ctkmsg.CTkMessagebox(message="Connexion Échouée", icon="cancel", option_1="Annuler")

        except Exception as e:
            print("Erreur de connexion:", e)


    windows_connexion = ctk.CTk()
    windows_connexion.title("SNT LABO")
    windows_connexion.geometry("600x400")

    # Creation de la frame
    frame_authentication = ctk.CTkFrame(windows_connexion, fg_color="transparent")

    # Creation des labels
    label_nom = ctk.CTkLabel(windows_connexion, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()

    label_nom = ctk.CTkLabel(frame_authentication, text="Veuillez entrer vos identifiants de connexion", fg_color="transparent", font=("Arial", 20))
    label_nom.pack(padx=10, pady=10)

    entre_login = ctk.CTkEntry(frame_authentication, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Login')
    entre_login.pack()

    entre_mdp = ctk.CTkEntry(frame_authentication, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Mot de passe')
    entre_mdp.pack(pady=10)

    btn_connexion = ctk.CTkButton(frame_authentication, text="Connexion", fg_color="grey", font=("Arial", 20), command=verif,width=300)
    btn_connexion.pack(pady=10)

    frame_authentication.pack(pady=50)

    windows_connexion.mainloop()
def mainframe():

    def retour():
        windows.destroy()
        connexion_user()
    def ajouter():
        windows.destroy()
        ajout_user()
    def modifier():
        windows.destroy()
        modif_user()
    def supprimmer():
        windows.destroy()
        suppr_user()
    def lister():
        windows.destroy()
        list_user()
    windows = ctk.CTk()
    windows.title("SNT LABO")
    windows.geometry("600x400")

    # Creation de la frame
    frame_btn_choix = ctk.CTkFrame(windows, fg_color="transparent")

    # Creation des labels
    label_nom = ctk.CTkLabel(windows, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady=40)

    btn_ajout_user = ctk.CTkButton(frame_btn_choix, text="Ajouter un utilisateur", fg_color="transparent", font=("Arial", 20),command=ajouter).grid(row=0, column=0, padx=10, pady=10)
    btn_modif_user = ctk.CTkButton(frame_btn_choix, text="Modifier un utilisateur", fg_color="transparent", font=("Arial", 20),command=modifier).grid(row=0, column=1, padx=10, pady=10)
    btn_suppr_user = ctk.CTkButton(frame_btn_choix, text="Supprimer un utilisateur", fg_color="transparent", font=("Arial", 20),command=supprimmer).grid(row=1, column=0, padx=10, pady=10)
    btn_list_user = ctk.CTkButton(frame_btn_choix, text="Lister les utilisateurs", fg_color="transparent", font=("Arial", 20),command=lister).grid(row=1, column=1, padx=10, pady=10)
    btn_quit = ctk.CTkButton(frame_btn_choix, text="Quitter", fg_color="transparent", font=("Arial", 20), command=retour).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    frame_btn_choix.pack(pady=30)

    windows.mainloop()
def ajout_user():
    def ajouter_user():
        try:
            user = User(enter_nom.get(), enter_prenom.get(), enter_email.get(), enter_num_tel.get(), enter_droit.get(), entere_role.get())
            user.genrate_login()
            user.generate_password(8)
            curseur.execute('INSERT INTO users (nom, prenom, email, num_tel, role, droit,login, password) VALUES (?,?,?,?,?,?,?,?)', (user.get_nom(), user.get_prenom(), user.get_email(), user.get_num_tel(), user.get_role(), user.get_droit(), user.get_login(), hashlib.sha256(user.get_password().encode()).hexdigest()))
            connexion.commit()
            ctkmsg.CTkMessagebox(message="Ajout Reussi", icon="check",option_1="Thanks")

        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
            windows.destroy()
            mainframe()
    windows = ctk.CTk()
    windows.title("SNT LABO")
    windows.geometry("600x550")

    # Creation de la frame
    frame_ajout_user = ctk.CTkFrame(windows, fg_color="transparent")

    # Creation des labels
    label_nom = ctk.CTkLabel(windows, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()

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

    ctk.CTkButton(frame_ajout_user, text="Ajouter", fg_color="grey", font=("Arial", 20),command=ajouter_user,width=300).pack(pady=10)

    frame_ajout_user.pack(pady=50)

    windows.mainloop()
    mainframe()
def modif_user():
    def modifier_user():
        try:
            data = curseur.execute('SELECT * FROM users WHERE login = ?', (enter_nom.get(),)).fetchall()
            user_trouve = False
            for user_data in data:
                if user_data[7] == enter_nom.get():
                    user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6])
                    if option_menu.get() == "Nom":
                        user.set_nom(enter_modif.get())
                        curseur.execute('UPDATE users SET nom = ? WHERE login = ?', (user.get_nom(), enter_nom.get()))
                    if option_menu.get() == "Prenom":
                        user.set_prenom(enter_modif.get())
                        curseur.execute('UPDATE users SET prenom = ? WHERE login = ?', (user.get_prenom(), enter_nom.get()))
                    if option_menu.get() == "Email":
                        user.set_email(enter_modif.get())
                        curseur.execute('UPDATE users SET email = ? WHERE login = ?', (user.get_email(), enter_nom.get()))
                    if option_menu.get() == "Numero de telephone":
                        user.set_num_tel(enter_modif.get())
                        curseur.execute('UPDATE users SET num_tel = ? WHERE login = ?', (user.get_num_tel(), enter_nom.get()))
                    if option_menu.get() == "Droit":
                        if enter_modif.get() not in ['md', 'cm', 'etc']:
                            ctkmsg.CTkMessagebox(message="Modification échoué", icon="cancel", option_1="Cancel")
                        else:
                            user.set_droit(enter_modif.get())
                            curseur.execute('UPDATE users SET droit = ? WHERE login = ?', (user.get_droit(), enter_nom.get()))
                    if option_menu.get() == "Role":
                        user.set_role(enter_modif.get())
                        curseur.execute('UPDATE users SET role = ? WHERE login = ?', (user.get_role(), enter_nom.get()))
                    connexion.commit()
            ctkmsg.CTkMessagebox(message="Modification échoué", icon="cancel", option_1="Cancel")

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")


    windows = ctk.CTk()
    windows.title("SNT LABO")
    windows.geometry("600x550")

    # Creation de la frame
    frame_modif_user = ctk.CTkFrame(windows, fg_color="transparent")

    # Creation des labels
    label_nom = ctk.CTkLabel(windows, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
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
    windows.mainloop()
    mainframe()
def suppr_user():
    def supprimer_user():
        try:
                curseur.execute('DELETE FROM users WHERE login = ?', (enter_nom.get(),))
                connexion.commit()

                ctkmsg.CTkMessagebox(message="Suppression Réussie", icon="check", option_1="Thanks")

        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

        # Appel de mainframe() avant de détruire la fenêtre



    windows = ctk.CTk()
    windows.title("SNT LABO")
    windows.geometry("600x550")

    # Création de la frame
    frame_suppr_user = ctk.CTkFrame(windows, fg_color="transparent")

    # Création des labels
    label_nom = ctk.CTkLabel(windows, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack(pady = 40)

    enter_nom = ctk.CTkEntry(frame_suppr_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='login')
    enter_nom.pack(pady=10)

    btn_supprimer = ctk.CTkButton(frame_suppr_user, text="Supprimer", fg_color="grey", font=("Arial", 20), command=supprimer_user,width=300)
    btn_supprimer.pack(pady=10)

    frame_suppr_user.pack(pady=50)
    windows.mainloop()
    mainframe()
def list_user():

    data = curseur.execute('SELECT * FROM users').fetchall()
    windows = ctk.CTk()
    windows.title("SNT LABO")
    windows.geometry("1500x550")

    # Creation de la frame
    frame_list_user = ctk.CTkFrame(windows, fg_color="transparent")

    # Creation des labels
    label_nom = ctk.CTkLabel(frame_list_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()
    for user in data:
        label_nom = ctk.CTkLabel(frame_list_user, text=f'Nom : {user[1]} Prenom : {user[2]} Email : {user[3]} Numéro de téléphone : {user[4]} Rôle : {user[5]} Droit : {user[6]} Login : {user[7]}', fg_color="transparent", font=("Arial", 20))
        ctk.CTkLabel(frame_list_user, text="---------------------------------------------", fg_color="transparent", font=("Arial", 20)).pack()
        label_nom.pack(padx=10, pady=10)




    frame_list_user.pack(pady=50)
    windows.mainloop()
    mainframe()
