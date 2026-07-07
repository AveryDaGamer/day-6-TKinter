#1 Clicking a Button -- Handled with "Command=" 
#2 Typing a key -- Handled with ".bind()"
#3 Moving the mouse -- Also Handled with ".bind()"
#4 Selecting a Radiobutton -- Also with "Command=". It checks the shared variable 
#5 Closing the Window -- Handled with the "window.protocol()"

import os
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

def submit_form():
    name=name_entry.get().strip()
    age_text=age_entry.get().strip()
    if name=="":
        messagebox.showerror("Error, Please enter your name")
        return
    try:
        age=int(age_text)
    except ValueError:
        messagebox.showerror("Age must be a valid number")
    
