# Import the tkinter library
from tkinter import *

# Create a tkinter window
pro = Tk()

# Set the window title and size
pro.title('LOGIN SYSTEM')
pro.geometry('500x500')
pro.resizable(False, False)  # Prevent window resizing
pro.config(background='#D5D8DC')  # Set the background color

# Set the window icon (make sure to provide the correct path to the icon file)
pro.iconbitmap('C:\\Users\\TechSupp\\Desktop\\ico.ico')

# Create a label for the title
title = Label(pro, text='LOGIN SYSTEM', font=('Courier', 15), bg='black', fg='white')
title.pack(fill=X)  # Fill the label horizontally

# Create a frame to contain the login elements
fr1 = Frame(pro, width=300, height=350, bg='white')
fr1.pack(pady=50, padx=100)  # Adjust padding values as needed

# Load an image and display it in a label
photo = PhotoImage(file="C:\\Users\\TechSupp\\Desktop\\log.png")
panal = Label(pro, image=photo, bg='white')
panal.place(x=200, y=79)

# Create labels for username and password
lab1 = Label(fr1, text='USERNAME:', font=('Courier', 15), bg='white')
lab1.place(x=10, y=140)

lab2 = Label(fr1, text='PASSWORD:', font=('Courier', 15), bg='white')
lab2.place(x=10, y=170)

# Create entry widgets for username and password
en1 = Entry(fr1)
en1.place(x=134, y=145)

en2 = Entry(fr1)
en2.place(x=134, y=185)

# Create login and signin buttons
bt1 = Button(fr1, text='LOGIN', font=('Courier', 15), bg='#A3E4D7', width='11')
bt1.place(x=13, y=260)

bt2 = Button(fr1, text='SIGNIN', font=('Courier', 15), bg='#F9E79F', width='11')
bt2.place(x=155, y=260)

# Create a checkbox for "Forget Password"
c1 = Checkbutton(fr1, text='FORGET PASSWORD!', font=('Courier', 10), bg='white')
c1.place(x=70, y=220)

# Create a label for developer information
pw = Label(fr1, text='DEVELOPED BY Asma Al Jabri', font=('Courier', 8), bg='white')
pw.place(x=60, y=330)

# Start the tkinter main loop
pro.mainloop()
