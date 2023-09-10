
from tkinter import * 

# Create the main window
pro = Tk()
pro.geometry("400x500")

# Create a horizontal Scale widget with values from 1 to 100
scale1 = Scale(pro, from_=1, to=100, orient=HORIZONTAL)
scale1.pack()

# Create a vertical Scale widget with values from 1 to 100
scale2 = Scale(pro, from_=1, to=100, orient=VERTICAL)
scale2.place(x=10, y=10)

# Create another horizontal Scale widget
scale3 = Scale(pro, from_=1, to=100, orient=HORIZONTAL)
scale3.place(x=10, y=100)


# Start the main event loop, allowing the GUI to be displayed and interacted with
pro.mainloop()

# In this code:

# We create a Tkinter window with a size of 400x500 pixels.
# We create a horizontal Scale widget (scale1) with values ranging from 1 to 100 and 
# pack it into the window.
# We create a vertical Scale widget (scale2) with the same value range and place it at 
# coordinates (10, 10) within the window.
# Another horizontal Scale widget (scale3) is created and placed at coordinates (10, 100)
# within the window.