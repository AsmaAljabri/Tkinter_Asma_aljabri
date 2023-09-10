from tkinter import *

# Create the main windows
pro1 = Tk()
pro1.title("First Window")

pro2 = Tk()
pro2.title("Second Window")

pro3 = Tk()
pro3.title("Third Window")

# Raise the first window in the stacking order
pro1.lift()

# Display the second window as an icon
pro2.iconify()

# Lower the third window in the stacking order
pro3.lower()


# Query or set the state of this widget as one of normal,
#  icon, iconic (see wm_iconwindow), withdrawn, or zoomed (Windows only).
# Set the state of the second window to "normal" (same as Iconify)
pro2.state("normal") # same as Iconify

# Start the main event loop for the first window
pro1.mainloop()



