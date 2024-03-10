
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import scrolledtext

class viewname:
    def __init__(self, parent):
        self.parent = parent
        self.directory = None  # Default directory
        self.handler=None
   

    def set_directory(self, directory):
        self.directory = directory
        self.key= directory
    def set_handler(self,handler):
        self.handler= handler

    def saved_filename(self):
        if not self.directory:
            print("Error: Directory not set.")
            return

        self.popup = tk.Toplevel(self.parent)
        self.popup.title("List of Saved Input Names")
        self.popup.geometry("600x300")
        self.popup.resizable(True, True)

        self.listbox = tk.Listbox(self.popup)
        self.listbox.pack(fill="both", expand=True)

        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                filename_without_extension = os.path.splitext(filename)[0]
                
                self.listbox.insert(tk.END, filename_without_extension)

        self.listbox.bind("<<ListboxSelect>>", self.viewer)

    
class AnotherViewName(viewname):
    def viewer(self, event=None):
        if not self.listbox.curselection():
            messagebox.showerror("Error", "No file selected!")
            return
    
        selected_file = self.listbox.get(self.listbox.curselection())
        self.selected_path = os.path.join(self.directory, f"{selected_file}.txt")
        with open(self.selected_path, 'r') as file:
            self.content = file.read()

        self.create_dialog()

    def create_dialog(self):
        self.dialog = tk.Toplevel()
        self.dialog.title("Saved Inputs")
        self.dialog.geometry("610x300")

        text_widget = scrolledtext.ScrolledText(self.dialog, font=('Monospac821 BT', 11), bg="#545454", fg="white", bd=5, height=15, width=50)
        text_widget.insert(tk.INSERT, self.content)
        text_widget.place(x=10, y=10)

        button_use = tk.Button(self.dialog, text="Use", command=self.used, font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C")
        button_use.place(x=490, y=10)
        D_use = tk.Button(self.dialog, text="Delete", command=self.delete, font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C")
        D_use.place(x=490, y=55)

        self.dialog.bind("<Destroy>", lambda event: self.popup.deiconify())

    def delete(self):
        os.remove(self.selected_path)
        messagebox.showinfo("Success", "File deleted successfully!")
        self.dialog.destroy()
        self.listbox.delete(tk.ACTIVE)
            
    def used(self):
       
        self.handler.delete("1.0", tk.END)  # Clear the text widget
        self.handler.insert(tk.INSERT, self.content)  # Insert the content
        self.dialog.destroy()
        self.popup.destroy() 
        
class AnotherViewgroups(viewname):
    def viewer(self, event=None):
        if not self.listbox.curselection():
            messagebox.showerror("Error", "No file selected!")
            return
    
        selected_file = self.listbox.get(self.listbox.curselection())
        self.selected_path = os.path.join(self.directory, f"{selected_file}.txt")
        with open(self.selected_path, 'r') as file:
            content = file.read()

        self.dialog = tk.Toplevel()
        self.dialog.title("File Content")
        self.dialog.geometry("610x300")

        text_widget = scrolledtext.ScrolledText(self.dialog, font=('Monospac821 BT', 11), bg="#545454", fg="white", bd=5, height=15, width=50)
        text_widget.insert(tk.INSERT, content)
        text_widget.place(x=10, y=10)

        delete_btn = tk.Button(self.dialog, text="Delete", command=self.delete, font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C")
        delete_btn.place(x=490, y=10)
        self.dialog.bind("<Destroy>", lambda event: self.popup.deiconify())

    def delete(self):
       
            os.remove(self.selected_path)
            messagebox.showinfo("Success", "File deleted successfully!")
        
            self.dialog.destroy()
        # Calls the popup method to perform additional actions
    
            self.listbox.delete(tk.ACTIVE)
