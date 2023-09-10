# Import the necessary modules from tkinter
from tkinter import *

# Create a tkinter window
root = Tk()

# Set the initial window size
root.geometry('500x500')

# Load an image file (replace with the actual path to your image)
photo = PhotoImage(file="C:\\Users\\TechSupp\\Desktop\\pyt.png")

# Create a Label widget and display the loaded image using the 'image' parameter
panel = Label(root, image=photo)

# Pack the Label widget to display the image in the window
panel.pack()

# Start the tkinter main loop to display the window
root.mainloop()
