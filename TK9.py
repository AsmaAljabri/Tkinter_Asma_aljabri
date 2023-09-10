from tkinter import * 
from tkinter import ttk

# Create the main window
pro = Tk()
pro.geometry("400x250")

# Create a Menubutton widget with the label 'Learn' and relief 'groove'
menu1 = Menubutton(pro, text='Learn', relief='groove')
menu1.pack()

# Create a Menu widget to populate the Menubutton
submenu = Menu(menu1)
menu1['menu'] = submenu 

# Add checkbuttons to the submenu for different subjects
submenu.add_checkbutton(label='HTML')
submenu.add_checkbutton(label='C++')
submenu.add_checkbutton(label='CSS')
submenu.add_checkbutton(label='Python')

# Create a Menubar
menubar = Menu(pro)

# Create a Menu and add commands for file operations
file_menu = Menu(menubar)
file_menu.add_command(label='New')  # Command for creating a new file
file_menu.add_command(label='Open')  # Command for opening an existing file
file_menu.add_command(label='Save')  # Command for saving the current file
file_menu.add_command(label='Save As')  # Command for saving with a different name
file_menu.add_command(label='Close')  # Command for closing the application

# Add a separator to visually separate file operations from exit command
file_menu.add_separator()

# Add an exit command to gracefully quit the application when selected
file_menu.add_command(label='Exit', command=pro.quit)

# Add the file menu to the menubar
menubar.add_cascade(label='File', menu=file_menu)

# Configure the main window to use the menubar
pro.config(menu=menubar)

# Start the main event loop, allowing the GUI to be displayed and interacted with
pro.mainloop()
