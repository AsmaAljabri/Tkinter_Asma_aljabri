from tkinter import * 

# Create the main window
pro = Tk()
pro.geometry("800x500")

# Create the first frame
frame1 = Frame(width='390', height='497', bg='gray')
frame1.place(x=1, y=1)
# The above lines create a Frame widget named 'frame1' with a width of 390 pixels,
# height of 497 pixels, and a background color of gray. The place() method is used
# to position the frame at coordinates (1, 1) within the main window.

# Create the second frame
frame2 = Frame(width='390', height='497', bg='black')
frame2.place(x=395, y=1)
# Similarly, this creates another Frame widget named 'frame2' with the same dimensions
# but with a background color of black. It's placed at coordinates (395, 1) within
# the main window.

pro.mainloop()
# The main event loop is started, allowing the GUI to be displayed and interacted with.
