import tkinter as tk
class Signup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

      

        # Username and Password Entry
        self.login_label = tk.Label(self, text="Sign UP", font=('Monospac821 BT', 17), fg="black", bg="#FEFFD5")
        self.login_label.place(x=565, y=150)
        
     