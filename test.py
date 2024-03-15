import customtkinter

windows = customtkinter.CTk()
windows.title('Connexion')

frame_test = customtkinter.CTkScrollableFrame(windows, fg_color='transparent')
frame_test.pack(fill='both', expand=True)

label = customtkinter.CTkLabel(frame_test, text='Connexion', font=('Arial', 20))
label.pack(pady=10)

label_login = customtkinter.CTkLabel(frame_test, text='Login', font=('Arial', 15))
label_login.pack(pady=10)

windows.mainloop()