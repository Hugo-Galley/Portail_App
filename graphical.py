import customtkinter as ctk
import CTkMessagebox as ctkmsg
from tkinter import messagebox

def connexion():
    def verif():
        try:
            if entre_login.get() == "admin" and entre_mdp.get() == "admin":
                 ctkmsg.CTkMessagebox(message="Connexion Reussi", icon="check", option_1="Thanks")

        except Exception as e:
            print("Erreur de connexion:", e)


    windows = ctk.CTk()
    windows.title("SNT LABO")
    windows.geometry("600x400")

    # Creation de la frame
    frame_authentication = ctk.CTkFrame(windows, fg_color="transparent")

    # Creation des labels
    label_nom = ctk.CTkLabel(windows, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()

    label_nom = ctk.CTkLabel(frame_authentication, text="Veuillez entrer vos identifiants de connexion", fg_color="transparent", font=("Arial", 20))
    label_nom.pack(padx=10, pady=10)

    entre_login = ctk.CTkEntry(frame_authentication, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Login')
    entre_login.pack()

    entre_mdp = ctk.CTkEntry(frame_authentication, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Mot de passe')
    entre_mdp.pack(pady=10)

    btn_connexion = ctk.CTkButton(frame_authentication, text="Connexion", fg_color="transparent", font=("Arial", 20), command=verif)
    btn_connexion.pack(pady=10)

    frame_authentication.pack(pady=50)

    windows.mainloop()
    mainframe()
def mainframe():

    def retour():
        windows.destroy()
        connexion()
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
    label_nom.pack()

    btn_ajout_user = ctk.CTkButton(frame_btn_choix, text="Ajouter un utilisateur", fg_color="transparent", font=("Arial", 20),command=ajouter).grid(row=0, column=0, padx=10, pady=10)
    btn_modif_user = ctk.CTkButton(frame_btn_choix, text="Modifier un utilisateur", fg_color="transparent", font=("Arial", 20),command=modifier).grid(row=0, column=1, padx=10, pady=10)
    btn_suppr_user = ctk.CTkButton(frame_btn_choix, text="Supprimer un utilisateur", fg_color="transparent", font=("Arial", 20),command=supprimmer).grid(row=1, column=0, padx=10, pady=10)
    btn_list_user = ctk.CTkButton(frame_btn_choix, text="Lister les utilisateurs", fg_color="transparent", font=("Arial", 20),command=lister).grid(row=1, column=1, padx=10, pady=10)
    btn_quit = ctk.CTkButton(frame_btn_choix, text="Quitter", fg_color="transparent", font=("Arial", 20), command=retour).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    frame_btn_choix.pack(pady=50)

    windows.mainloop()

def ajout_user():
    def ajouter_user():
        try:
            if enter_nom.get() == "admin":
                ctkmsg.CTkMessagebox(message="Connexion Reussi", icon="check",option_1="Thanks")
                windows.destroy()
                mainframe()
            else:
                ctkmsg.CTkMessagebox(message="Connexion échoué", icon="cancel", option_1="Cancel")
                windows.destroy()
                mainframe()
        except Exception as e:
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

    btn_connexion = ctk.CTkButton(frame_ajout_user, text="Ajouter", fg_color="transparent", font=("Arial", 20),command=ajouter_user).pack(pady=10)

    frame_ajout_user.pack(pady=50)

    windows.mainloop()
def modif_user():
    def modifier_user():
        try:
            if enter_nom.get() == "admin":
                ctkmsg.CTkMessagebox(message="Connexion Reussi", icon="check",option_1="Thanks")

            else:
                ctkmsg.CTkMessagebox(message="Connexion échoué", icon="cancel", option_1="Cancel")

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")


    windows = ctk.CTk()
    windows.title("SNT LABO")
    windows.geometry("600x550")

    # Creation de la frame
    frame_modif_user = ctk.CTkFrame(windows, fg_color="transparent")

    # Creation des labels
    label_nom = ctk.CTkLabel(frame_modif_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()

    enter_nom = ctk.CTkEntry(frame_modif_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='login')
    enter_nom.pack(pady=10)

    options = ["Nom", "Prenom", "Email", "Numero de telephone", "Droit", "Role"]
    option_menu = ctk.CTkOptionMenu(frame_modif_user, values=options)
    option_menu.pack(pady=10)

    enter_modif = ctk.CTkEntry(frame_modif_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='Nouvelle Valeur')
    enter_modif.pack(pady=10)

    btn_connexion = ctk.CTkButton(frame_modif_user, text="Modifier", fg_color="transparent", font=("Arial", 20), command=modifier_user)
    btn_connexion.pack(pady=10)

    frame_modif_user.pack(pady=50)
    windows.mainloop()
    mainframe()
def suppr_user():
    def supprimer_user():
        try:
            if enter_nom.get() == "admin":
                ctkmsg.CTkMessagebox(message="Suppression Réussie", icon="check", option_1="Thanks")
            else:
                ctkmsg.CTkMessagebox(message="Suppression échouée", icon="cancel", option_1="Cancel")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

        # Appel de mainframe() avant de détruire la fenêtre



    windows = ctk.CTk()
    windows.title("SNT LABO")
    windows.geometry("600x550")

    # Création de la frame
    frame_suppr_user = ctk.CTkFrame(windows, fg_color="transparent")

    # Création des labels
    label_nom = ctk.CTkLabel(frame_suppr_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()

    enter_nom = ctk.CTkEntry(frame_suppr_user, fg_color="transparent", font=("Arial", 20), width=300, placeholder_text='login')
    enter_nom.pack(pady=10)

    btn_supprimer = ctk.CTkButton(frame_suppr_user, text="Supprimer", fg_color="transparent", font=("Arial", 20), command=supprimer_user)
    btn_supprimer.pack(pady=10)

    frame_suppr_user.pack(pady=50)
    windows.mainloop()
    mainframe()

def list_user():
    windows = ctk.CTk()
    windows.title("SNT LABO")
    windows.geometry("600x550")

    # Creation de la frame
    frame_list_user = ctk.CTkFrame(windows, fg_color="transparent")

    # Creation des labels
    label_nom = ctk.CTkLabel(frame_list_user, text="SNT LABO", fg_color="transparent", font=("Arial", 40))
    label_nom.pack()

    label_nom = ctk.CTkLabel(frame_list_user, text="Liste des utilisateurs", fg_color="transparent", font=("Arial", 20))
    label_nom.pack(padx=10, pady=10)


    frame_list_user.pack(pady=50)
    windows.mainloop()

mainframe()