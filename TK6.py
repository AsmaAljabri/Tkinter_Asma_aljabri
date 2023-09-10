from tkinter import * 
from tkinter import ttk

# Create the main window
pro = Tk()
pro.geometry("600x400")

# Create a ComboBox for selecting gender
gender_combobox = ttk.Combobox(pro, 
                                value=('Male', 'Female'), 
                                state='readonly')
gender_combobox.place(x=1, y=1)
# The above code creates a ComboBox widget for selecting gender. The 'value' parameter specifies
# the available options: 'Male' and 'Female'. The 'state' is set to 'readonly' to ensure that
# users can only select values from the list and cannot manually input text.

# Create a ComboBox for selecting countries
country_combobox = ttk.Combobox(pro, 
                                 value=('Oman', 'UAE', 'USA', 'UK', 'Malaysia'), 
                                 state='readonly')
country_combobox.place(x=1, y=35)
# This ComboBox allows users to select a country from the provided list of options. Again, the 'state'
# is set to 'readonly' to enforce selection from the predefined list.

pro.mainloop()
# The main event loop is started, allowing the GUI to be displayed and interacted with.


# ComboBox (ttk.Combobox) in Tkinter:

# A ComboBox, created using ttk.Combobox, is a versatile widget for presenting a dropdown list of options to users. Here's a breakdown of the code:

# gender_combobox and country_combobox represent two ComboBox widgets.
# value parameter defines the available choices within each ComboBox.
# Setting the state to 'readonly' ensures that users can only choose 
# options from the provided list and cannot manually enter values.
# The place() method positions the ComboBox widgets in the main window.
# Using ComboBoxes is a user-friendly way to allow users to make selections from
# predefined options, making data entry more efficient and reducing the chance of input errors.
