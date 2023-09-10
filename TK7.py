from tkinter import * 
from tkinter import ttk

# Create the main window
pro = Tk()
pro.geometry("600x400")

# Create a Listbox widget
list1 = Listbox(pro, width=10, height=7)
# The above line creates a Listbox widget named 'list1'. It's configured to have a width of 10 characters
# and a height of 7 visible items.

# Insert items into the Listbox
list1.insert(0, 'one')
list1.insert(1, 'two')
list1.insert(2, 'three')
list1.insert(3, 'four')
list1.insert(4, 'five')
# The above lines insert five items ('one', 'two', 'three', 'four', 'five') into the Listbox.
# The first parameter is the index at which to insert the item.

list1.pack()
# The Listbox is packed into the main window. It will expand to fit its contents.

pro.mainloop()
# The main event loop is started, allowing the GUI to be displayed and interacted with.

# Listbox in Tkinter:

# A Listbox is a widget used to display a list of items from which the user can select
# one or more options. Here's an explanation of the code:

# list1 is a Listbox widget with a specified width and height.
# The insert() method is used to add items ('one', 'two', 'three', 'four', 'five') to the Listbox. 
# The first parameter indicates the index at which the item should be inserted.
# list1.pack() places the Listbox in the main window, allowing it to expand based on its content.
