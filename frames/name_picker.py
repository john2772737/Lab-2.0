import tkinter as tk
from PIL import Image, ImageTk
import random as rand
from tkinter import messagebox
from keypressedhandler import KeyPressHandler
from tkinter import messagebox

class NamePicker(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.generated= False

        # Whole Background
        self.bg_frame = tk.Frame(self, height=650, width=1200)
        self.bg_frame.pack(fill="both", expand=True)
    
        #Background Image
        bg_image_path = "images/bg3.jpg"
        self.img = Image.open(bg_image_path)
        self.img = self.img.resize((1200, 575))
        self.img = ImageTk.PhotoImage(self.img)
        self.bg_label = tk.Label(self.bg_frame, image=self.img)
        self.bg_label.image = self.img
        self.bg_label.place(x=0, y=75)

        #Input Name Label
        self.input_name_label = tk.Label(self.bg_frame, text="Input Names:  ", font=('Monospac821 BT', 15), fg="black", bg="#FEFFD5")
        self.input_name_label.place(x=270, y=275)
        
        #User Input handler
        self.text_handler= tk.Text(self.bg_frame, font=('Monospac821 BT', 13), height=11, width=35, bg="#545454", fg="white", bd=5)
        self.text_handler.place(x=265, y=300)
        self.text_handler.bind("<Key>", KeyPressHandler().on_keypress)


        self.option_label = tk.Label(self.bg_frame, text="No. of Names:", font=('Monospac821 BT', 13), fg="black", bg="#FEFFD5")
        self.option_label.place(x=270, y=535)

        self.spinbox = tk.Spinbox(self.bg_frame, from_=1, to=10, font=('Monospac821 BT', 13, ' bold'), fg="white", width=15, bd=2, bg="#545454")
        self.spinbox.place(x=265, y=560)

        self.pick_button = tk.Button(self.bg_frame, text="Pick", font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C" ,command=self.pick_name)
        self.pick_button.place(x=265, y=595)

        #Results Label
        self.results_label = tk.Label(self.bg_frame, text="Results:", font=('Monospac821 BT', 15), fg="black", bg="#FEFFD5")
        self.results_label.place(x=670, y=275)
       
        #Sample Results Box
        self.results_label = tk.Label(self.bg_frame, bg="#545454", height=15, width=55, bd=5)
        self.results_label.place(x=665, y=300)

        self.reset_button = tk.Button(self.bg_frame, text="Reset", font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C",command=self.reset)
        self.reset_button.place(x=805, y=570)

        #Instruction Message
        self.instruction_label = tk.Label(self.bg_frame, text="Instructions:", font=('Monospac821 BT', 15), fg="black", bg="#FEFFD5")
        self.instruction_label.place(x=55, y=275)
            
        self.instruction_label1 = tk.Label(self.bg_frame, text='Enter names in the provided box, choose how many names you want, and click “pick”. Click “Reset” if you want to try again.', font=('Monospac821 BT', 11), fg="black", bg="#FEFFD5", wraplength=220 )
        self.instruction_label1.place(x=35, y=325)

        self.instruction_label2 = tk.Label(self.bg_frame, text='Note: Use comma after each name.', font=('Monospac821 BT', 11), fg="red", bg="#FEFFD5", wraplength=220 )
        self.instruction_label2.place(x=35, y=440)

        self.return_button = tk.Button(self.bg_frame, text="Main", font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C")
        self.return_button.place(x=50, y=80)
        
        
    def change_frame(self):
        self.change_frame('Main')

    def text_getter(self,count):
        self.list_name= self.text_handler.get("1.0", "end-1c").strip()
        self.names = self.list_name.replace(',', ' ').split()

        if count > len(self.names):   
            messagebox.showerror("Error", "Sample size larger than population.")
            return None
        
        self.generated = rand.sample(self.names,count) 
      
        bullet_list = "\n".join("• " + item for item in self.generated)
        self.results_label.config(text=bullet_list, fg='White')

        for item in self.generated:
            self.names.remove(item)
 
        updated_list = ", ".join(self.names)
        self.text_handler.delete("1.0", "end-1c")
        self.text_handler.insert("1.0", updated_list)
        
    
    def pick_name(self):
        self.list_name = self.text_handler.get("1.0", "end-1c").strip()

        if not self.list_name:
            messagebox.showwarning("Warning", "No name on the list.")
            return None

        if  len(self.list_name.split(',')) < 2:
            messagebox.showwarning("Warning", "Please enter more names.")
            return None

        if  self.list_name.endswith(","):
                messagebox.showwarning("Warning", "You have entered a comma at the end, expecting more names.")
                return None
        
        spin_value = self.spinbox.get()
        
        count = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10
        }
        
        count = count.get(spin_value)
        
        if count is not None:
            self.text_getter(count)
            self.generated=True

    def reset(self):
        if not self.generated:
            messagebox.showwarning("Warning", "Please generate names before resetting.")
            return
        confirm_reset = messagebox.askyesno("Confirmation", "Are you sure you want to reset?")
        if confirm_reset:
            self.names.clear()
            self.text_handler.delete("1.0", "end-1c")
            self.results_label.config(text="")