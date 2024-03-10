import tkinter as tk
from PIL import Image, ImageTk
import random as rand
from tkinter import messagebox
from tkinter import scrolledtext
from keypressedhandler import KeyPressHandler
import os
from tkinter import messagebox, simpledialog
from viewname import AnotherViewName,AnotherViewgroups

class GroupPicker(tk.Frame):
    def __init__(self, master):
            tk.Frame.__init__(self, master)

            self.generate_button_disabled = False  
            self.generated = False
            self.group_label_texts = []

         
            self.folder_names = {
            'groups': 'MyFolder',
            'input': 'input'
            }
         
            # Whole Background
            self.bg_frame = tk.Frame(self, height=650, width=1200)
            self.bg_frame.pack(fill="both", expand=True)

            #Background Image
            bg_image_path = "images/bg2.jpg"
            self.img = Image.open(bg_image_path)
            self.img = self.img.resize((1200, 575))
            self.img = ImageTk.PhotoImage(self.img)
            self.bg_label = tk.Label(self.bg_frame, image=self.img)
            self.bg_label.image = self.img
            self.bg_label.place(x=0, y=75)

            #Input Name Label
            self.input_name_label = tk.Label(self.bg_frame, text="Input Names:", font=('Monospac821 BT', 15), fg="black", bg="#FEFFD5")
            self.input_name_label.place(x=270, y=275)
            
            #User Input handler
            self.text_handler= tk.Text(self.bg_frame, font=('Monospac821 BT', 13), height=11, width=35, bg="#545454", fg="white", bd=5)
            self.text_handler.place(x=265, y=300)
            self.text_handler.bind("<Key>", KeyPressHandler().on_keypress)


            self.group_option_label = tk.Label(self.bg_frame, text="Groups:", font=('Monospac821 BT', 13), fg="black", bg="#FEFFD5")
            self.group_option_label.place(x=270, y=535)

            self.spinbox = tk.Spinbox(self.bg_frame, from_=2, to=6, font=('Monospac821 BT', 13, ' bold'), fg="white", width=15, bd=2, bg="#545454")
            self.spinbox.place(x=265, y=560)

            self.generate_button = tk.Button(self.bg_frame, text="Generate", font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C" ,command=self.pick_name)
            self.generate_button.place(x=265, y=595)

            self.save = tk.Button(self.bg_frame, text="Save group", font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C",command=self.saves )
            self.save.place(x=840, y=595)
            #Results Label
            self.results_label = tk.Label(self.bg_frame, text="Results:", font=('Monospac821 BT', 15), fg="black", bg="#FEFFD5")
            self.results_label.place(x=650, y=275)

            self.reset = tk.Button(self.bg_frame, text="Reset", font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C",command=self.resets)
            self.reset.place(x=725, y=595)

            self.history = tk.Button(self.bg_frame, text="View History", font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=12, bd=2, bg="#F2B84C" ,command=self.list_history)
            self.history.place(x=955, y=595)

            #Instruction Message
            self.instruction_label = tk.Label(self.bg_frame, text="Instructions:", font=('Monospac821 BT', 15), fg="black", bg="#FEFFD5")
            self.instruction_label.place(x=55, y=275)
            
            self.instruction_label1 = tk.Label(self.bg_frame, text='Enter names in the provided box, choose how many groups you want, and click "Generate." Click “Reset” if you want to generate again.', font=('Monospac821 BT', 11), fg="black", bg="#FEFFD5", wraplength=220 )
            self.instruction_label1.place(x=35, y=325)

            self.instruction_label2 = tk.Label(self.bg_frame, text='Note: Use comma after each name.', font=('Monospac821 BT', 11), fg="red", bg="#FEFFD5", wraplength=220 )
            self.instruction_label2.place(x=35, y=480)

            self.view_names = tk.Button(self.bg_frame, text="View Saved Names", font=('Monospac821 BT', 12, ' bold'), fg="black", height=1, width=16, bd=2, bg="#F2B84C" ,command=self.view_saved_names)
            self.view_names.place(x=380, y=595)

            self.return_button = tk.Button(self.bg_frame, text="Main", font=('Monospac821 BT', 13, ' bold'), fg="black", height=1, width=10, bd=2, bg="#F2B84C")
            self.return_button.place(x=50, y=80)
           

    def list_history(self):
        self.popup=AnotherViewgroups(self)
        folder=self.select_folder_path('groups')
        self.popup.set_handler(self.text_handler)
        self.popup.set_directory(folder)
        self.popup.saved_filename() 
        
    def view_saved_names(self):
        self.popup=AnotherViewName(self)
        folder=self.select_folder_path('input')
        self.popup.set_directory(folder)
        self.popup.set_handler(self.text_handler)
        self.popup.saved_filename()  
  

    def text_getter(self,count):

            self.list_name= self.text_handler.get("1.0", "end-1c").strip()
            self.nameg = self.list_name.replace(',', ' ').split() 
            self.generated = rand.sample(self.nameg,count) 
            self.bullet_list = "\n".join("• " + item for item in self.generated)
          
            
            for item in self.generated:
                self.nameg.remove(item)
    
            updated_list = ", ".join(self.nameg)
            self.text_handler.delete("1.0", "end-1c")
            self.text_handler.insert("1.0", updated_list)

            return self.bullet_list
        
    def pick_name(self):
            self.generated = True
           
            self.list_name= self.text_handler.get("1.0", "end-1c").strip()
            
            if not self.list_name:
                # Show a warning and return without disabling the button
                messagebox.showwarning("Warning", "No name on the list.")
                return None
            if  len(self.list_name.split(',')) < 2:
                messagebox.showwarning("Warning", "Please enter more names.")
                return None
            if  self.list_name.endswith(","):
                messagebox.showwarning("Warning", "you have entered an comma at the end, expecting more names.")
                return None

            self.spin_value = int(self.spinbox.get())
            columns_per_row = 3
            spacing = 150

            names = self.text_handler.get("1.0", "end-1c").strip().split(',')
            total_names = len(names)
            print(names)
            if self.spin_value > total_names:  # Compare with the length of nameg
                messagebox.showerror("Warning", "The number of groups is larger than the number of names inputted.")
                return None
            

        
            # Calculate the base number of names per group
            names_per_group = total_names // self.spin_value
            remainder = total_names % self.spin_value

            # Initialize the start index for name distribution
            start_idx = 0

            # Create an empty list to store group_label widgets
            self.group_labels = []

            for i in range(self.spin_value):
                row = i // columns_per_row
                col = i % columns_per_row

                x_value = 660 + col * (15 + spacing)
                y_value = 300 + row * (5 + spacing)

                # Determine the group size for this iteration
                group_size = names_per_group
                if i < remainder:
                    group_size += 1

                # Retrieve the list of names for the current group
                group_names = self.text_getter(group_size)

                # Construct the label text for the current group
                group_label_text = f"Group {i + 1}:\n{group_names}"

                # Create and place the label for the current group
                group_label = scrolledtext.ScrolledText(self.bg_frame, bg="#545454", fg="white", height=8, width=15)
                group_label.insert(tk.INSERT,group_label_text)
                group_label.place(x=x_value, y=y_value)

                # Append the created label to the list
                self.group_labels.append(group_label)

            self.text_handler.delete("1.0", "end-1c")
          
             # Disable the "Generate" button
            self.generate_button_disabled = True
      


            confirmation_save=messagebox.askyesno("Save","Do you want to save your Input Names?")

            if not confirmation_save:
                return None
            
            save_inputfile = os.path.expanduser("~/Documents")

            # Specify the name of the folder you want to create
            folder_name = "input"

            # Create the full path to the folder
            self.folderpath_input = os.path.join(save_inputfile, folder_name)
            
            if not os.path.exists(self.folderpath_input):
                os.makedirs(self.folderpath_input)

            
            while True:
                self.names_group = simpledialog.askstring("Create your File", "Input your File Name:")
                if self.names_group is None:
                    # User canceled the dialog
                    return

                filename = os.path.join(self.folderpath_input, f'{self.names_group}.txt')

                if not self.names_group:
                    messagebox.showwarning("Warning", "No File Name provided.")
                    return

                if os.path.exists(filename):
                    response = messagebox.askokcancel("Warning", "File Name already exists. Do you want to overwrite it?")
                    if not response:
                        continue  # Ask for input again

                data_save = ""
                for i, name in enumerate(names):
                    data_save += name
                    if i < len(names) - 1:
                        data_save += ","

                with open(filename, "w") as file:
                    file.write(data_save)
                
                messagebox.showinfo("Success", f"File '{self.names_group}.txt' saved successfully.")
                self.names_group.destroy()

    def saves(self):

        
        if not self.generated:
            # If groups haven't been generated, return without saving
            messagebox.showwarning("Warning", "Please generate groups before saving.")
            return
        
        path=self.select_folder_path('groups')
        while True:
            self.names_group = simpledialog.askstring("Create your File", "Input File Name:")
            if self.names_group is None:
                # User canceled the dialog
                return

            filename = os.path.join(path, f'{self.names_group}.txt')

            if not self.names_group:
                messagebox.showwarning("Warning", "No File Name provided.")
                return

            if os.path.exists(filename):
                response = messagebox.askokcancel("Warning", "File Name already exists. Do you want to overwrite it?")
                if not response:
                    continue  # Ask for input again

            # Prepare file content
            file_content = ""
            for label in self.group_labels:
                label_content = label.get("1.0", tk.END)
                file_content += label_content + "\n"
            print(file_content)
            # Write content to the file
            with open(filename, 'w') as file:
                file.write(file_content)

            messagebox.showinfo("Success", f"File '{self.names_group}.txt' saved successfully.")
            break  # Exit the loop after saving the file
  
    def resets(self):
        if not self.generated:
            # If groups haven't been generated, return without resetting
            messagebox.showwarning("Warning", "Please generate groups before resetting.")
            return

        # Ask for confirmation before resetting
        confirm_reset = messagebox.askyesno("Confirmation", "Are you sure you want to reset?")
        if confirm_reset:
            # Clear the list of names
            self.text_handler.delete("1.0", "end-1c")

            # Enable the "Generate" button
            self.generate_button_disabled = False
            self.generate_button.config(state=tk.NORMAL)

            # Destroy existing group labels
            for label in self.group_labels:
                label.destroy()
            self.group_labels = []

            # Reset the generated flag
            self.generated = False

    def select_folder_path(self, key):
        documents_path = os.path.expanduser("~/Documents")
        folder_name = self.folder_names.get(key)

        if folder_name:
            folder_path = os.path.join(documents_path, folder_name)
            # Check if the folder exists, if not, create it
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            return folder_path
        else:
            print("Folder key not found.")
            return None