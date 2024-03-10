import os
import tkinter as tk
from datetime import datetime

class FileBrowser:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def show_content(self, event):
        selected_file = self.listbox.get(self.listbox.curselection())
        with open(os.path.join(self.folder_path, selected_file), 'r') as file:
            content = file.read()
            content_popup = tk.Toplevel()
            content_popup.title(selected_file)
            content_text = tk.Text(content_popup)
            content_text.insert(tk.END, content)
            content_text.pack(fill="both", expand=True)

    def browse(self):
        root = tk.Tk()
        root.title("File Browser")
        root.geometry("600x400")

        # Create search frame
        search_frame = tk.Frame(root)
        search_frame.pack(fill="x", padx=10, pady=10)

        self.search_var = tk.StringVar()
        search_label = tk.Label(search_frame, text="Search by name:")
        search_label.pack(side="left")
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left", padx=5)
        search_button = tk.Button(search_frame, text="Search", command=self.search_files)
        search_button.pack(side="left", padx=5)

        # Create listbox with scrollbars
        list_frame = tk.Frame(root)
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.listbox.yview)

        # Bind double-click event to show_content function
        self.listbox.bind("<Double-Button-1>", self.show_content)

        # Populate listbox with file names and creation dates
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.folder_path, filename)
                creation_date = datetime.fromtimestamp(os.path.getctime(file_path))
                creation_date_str = creation_date.strftime("%Y-%m-%d %H:%M:%S")
                self.listbox.insert(tk.END, f"{filename} (Created: {creation_date_str})")

        root.mainloop()

    def search_files(self):
        search_term = self.search_var.get().strip()
        self.listbox.delete(0, tk.END)
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt") and search_term.lower() in filename.lower():
                file_path = os.path.join(self.folder_path, filename)
                creation_date = datetime.fromtimestamp(os.path.getctime(file_path))
                creation_date_str = creation_date.strftime("%Y-%m-%d %H:%M:%S")
                self.listbox.insert(tk.END, f"{filename} (Created: {creation_date_str})")


# Example usage:
if __name__ == "__main__":
    documents_path = os.path.expanduser("~/Documents/MyFolder")

            # Specify the name of the folder you want to create
    folder_name = "MyFolder"

            # Create the full path to the folder
            
    picker = FileBrowser(f"{documents_path}")
    picker.browse()