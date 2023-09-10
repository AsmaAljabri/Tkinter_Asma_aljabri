from tkinter import *

# Create the main windows
pro1 = Tk()
pro2 = Tk()
pro3 = Tk()

# Set titles for the windows
pro1.title("Home Window")
pro2.title("Shopping Cart Window")

# Set dimensions and positions for the windows
pro1.geometry("300x300+10+10")  # Width x Height + Left + Top
pro2.geometry("300x300+320+10")  # Width x Height + Left + Top

# Set background colors for the windows
pro1.config(background="gray")
pro2.config(background="purple")

# Start the main event loop for the first window
pro1.mainloop()
