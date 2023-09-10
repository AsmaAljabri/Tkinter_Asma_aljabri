# Import the necessary modules from tkinter
from tkinter import *
import tkinter as tk

# Create a tkinter window
pro = Tk()

# Set the initial window size
pro.geometry('500x500')

# Create a Text widget (text area) and pack it into the window
T = tk.Text(pro)
T.pack()

# Define the text content that you want to display in the Text widget
learn = """
LETS LEARN PYTHON
LETS LEARN C++
LETS LEARN JAVA
LETS LEARN SQL
PYTHON IS VERY EASY
"""

# Insert the 'learn' text into the Text widget at the end (tk.END)
T.insert(tk.END, learn)

# Start the tkinter main loop to display the window
pro.mainloop()
