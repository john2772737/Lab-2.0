import tkinter as tk

def toggle_password_visibility(password_entry, show_password_var):
        current_value = password_entry.get()
        password_entry.delete(0, tk.END)
        
        if show_password_var.get():
            password_entry.config(show="")
            show_password_var.set(False)
        else:
            password_entry.config(show="*")
            show_password_var.set(True)
            
        password_entry.insert(0, current_value)