import tkinter as tk
class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

      

        # Username and Password Entry
        self.login_label = tk.Label(self, text="Log In", font=('Monospac821 BT', 17), fg="black", bg="#FEFFD5")
        self.login_label.place(x=565, y=150)
        
        self.welcome_button= tk.Button(self,text="welcome",command=self.change_to_welcome)
        self.welcome_button.pack()

    def change_to_welcome(self):
        self.master.change_frame('welcome')