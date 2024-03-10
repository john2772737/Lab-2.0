from tkinter import messagebox

class KeyPressHandler:
    def __init__(self):
        self.caps_lock_on = False

    def on_keypress(self, event):
        # Get the pressed key
        pressed_key = event.char

        # Check if the Caps Lock key is on
        if event.keysym == "Caps_Lock":
            self.caps_lock_on = not self.caps_lock_on
            return

        # Check if the pressed key is Control or Shift
        if event.keysym in ["Control_L", "Control_R", "Shift_L", "Shift_R"]:
            return

        # Convert the character to uppercase if Caps Lock is on
        if self.caps_lock_on:
            pressed_key = pressed_key.upper()

        # Check if the pressed key is a letter, comma, or backspace
        if pressed_key.isalpha() or pressed_key == ',' or event.keysym == 'BackSpace':
            pass
        elif event.keysym == 'v' and (event.state & 4):  # Check if 'v' is pressed and Ctrl is also pressed
            pass  # Allow Ctrl+V for paste action
        elif event.keysym == 'c' and (event.state & 4):  # Check if 'v' is pressed and Ctrl is also pressed
            pass 
        elif event.keysym == 'x' and (event.state & 4):  # Check if 'v' is pressed and Ctrl is also pressed
            pass 
        elif event.keysym == 'a' and (event.state & 4):  # Check if 'v' is pressed and Ctrl is also pressed
            pass 
        
        
        else:
            # If the pressed key is not allowed, show an error message
            messagebox.showerror("Error", "Only letters, commas, and Caps Lock are allowed.")
            # Prevent the default action (inserting the character)
            return "break"
