import tkinter as tk

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.insert(0, self.placeholder)
        self.config(fg="#545454")  # Set text color to gray

        self.bind("<FocusIn>", self.clear_on_first_click)
        self.bind("<FocusOut>", self.restore_placeholder)

    def clear_on_first_click(self, event):
        current_text = self.get()

        # Check if the current text is the default placeholder text or empty
        if current_text == self.placeholder or not current_text.strip():
            self.delete(0, tk.END)  # Remove the placeholder text
            self.config(fg="#545454")  # Set text color to black

    def restore_placeholder(self, event):
        current_text = self.get().strip()

        # Check if the current text is empty
        if not current_text:
            self.delete(0, tk.END)
            self.insert(0, self.placeholder)
            self.config(fg="#545454")  # Set text color to gray

