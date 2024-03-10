import tkinter as tk
from frames.name_picker import NamePicker
from frames.group_picker import GroupPicker
from frames.Login import Login
from frames.sign_up import Signup
from frames.welcome import Welcome

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Random Picker Generator")
        self.geometry("1200x650")

        self.frames = {}
        self.frames['namepicker'] = NamePicker(self)
        self.frames['grouppicker'] = GroupPicker(self)
        self.frames['login']= Login(self)
        self.frames['signup']= Signup(self)
        self.frames['welcome']= Welcome(self)

        self.current_frame = None
        self.change_frame('login')



    def change_frame(self, name, **kwargs):
        if self.current_frame:
            self.current_frame.pack_forget()

        self.current_frame = self.frames[name]
        self.current_frame.pack(fill="both", expand=True)

    

root = MainWindow()
root.resizable(True, True)

root.mainloop()         
  
#root = MainWindow()
#root.resizable(False, False)
#root.mainloop()
