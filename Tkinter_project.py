#1 Clicking a Button -- Handled with "Command=" 
#2 Typing a key -- Handled with ".bind()"
#3 Moving the mouse -- Also Handled with ".bind()"
#4 Selecting a Radiobutton -- Also with "Command=". It checks the shared variable 
#5 Closing the Window -- Handled with the "window.protocol()"

import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get().strip()
    age_text = age_entry.get().strip()

    if name == "":
        messagebox.showerror("Error", "Please enter your name.")
        return

    try:
        age = int(age_text)
    except ValueError:
        messagebox.showerror("Error", "Age must be a whole number.")
        return

    messagebox.showinfo(
        "Form Submitted",
        f"Name: {name}\nAge: {age}"
    )

window = tk.Tk()
window.title("Simple Form")
window.geometry("300x200")

tk.Label(window, text="Name:").pack(pady=(15, 0))
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Age:").pack(pady=(10, 0))
age_entry = tk.Entry(window)
age_entry.pack()

submit_button = tk.Button(
    window,
    text="Submit",
    command=submit_form
)
submit_button.pack(pady=20)

window.mainloop()
