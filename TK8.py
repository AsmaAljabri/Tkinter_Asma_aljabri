from tkinter import * 
from tkinter import ttk

# Create the main window
pro = Tk()
pro.geometry("600x400")

# Create RadioButtons
# RadioButtons are used for mutually exclusive choices, where the user can select only one option from a group.

# Create the first RadioButton for 'male 1'
r1 = ttk.Radiobutton(pro, text='Male 1', value=1)   
r1.pack()
# The above code creates a RadioButton labeled 'Male 1' with a value of 1.

# Create the second RadioButton for 'female'
r2 = ttk.Radiobutton(pro, text='Female', value=2)   
r2.pack()
# This RadioButton is labeled 'Female' with a value of 2.

# Create the third RadioButton for 'male 2'
r3 = ttk.Radiobutton(pro, text='Male 2', value=3)   
r3.pack()
# This RadioButton is labeled 'Male 2' with a value of 3.

# Create Checkbuttons
# Checkbuttons allow users to select multiple options from a group.

# Create the first Checkbutton for 'first class'
ck1 = Checkbutton(pro, text='First Class')
ck1.pack()
# The above code creates a Checkbutton labeled 'First Class'.

# Create the second Checkbutton for 'second class'
ck2 = Checkbutton(pro, text='Second Class')
ck2.pack()
# This Checkbutton is labeled 'Second Class'.

# Create the third Checkbutton for 'third class'
ck3 = Checkbutton(pro, text='Third Class')
ck3.pack()
# This Checkbutton is labeled 'Third Class'.


pro.mainloop()
# The main event loop is started, allowing the GUI to be displayed and interacted with.


# RadioButtons in Tkinter:

# RadioButtons are a type of widget used for providing multiple choices, but only one option
#  can be selected at a time (mutually exclusive). In this code:

# r1, r2, and r3 represent three RadioButtons.
# text specifies the label or text associated with each RadioButton.
# value is a unique identifier for each RadioButton, which allows you to determine which 
# option the user has selected.


# Checkbuttons
# These Checkbuttons provide a way for users to select one or more classes. Users can click on a 
# Checkbutton to toggle its state (checked or unchecked). They are commonly used in forms where users
# need to make multiple selections or toggle options on and off.