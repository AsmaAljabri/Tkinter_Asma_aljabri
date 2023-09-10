
from tkinter import * 
from tkinter import ttk

# Create the main window
pro = Tk()
pro.geometry("500x400")



scbar1= Scrollbar(pro, orient= VERTICAL)
scbar1.pack(side= RIGHT, fill= Y)

scbar2= Scrollbar(pro, orient= HORIZONTAL )
scbar2.pack(side= BOTTOM, fill= X)

notebok = ttk.Notebook(pro)
notebok.pack()

f1 = Frame(notebok, width = '500', height = '100', bg = 'silver')
notebok.add(f1, text = 'Tools')

f2 = Frame(notebok, width = '500', height = '100',  bg = 'silver')
notebok.add(f2, text = 'display')

la1 = Label(f1,text= 'learn python',  bg = 'silver')
la1.pack()


la2 = Label(f1,text= 'learn C++',  bg = 'silver')
la2.pack()

notebok.select(f1)


sp = Spinbox(pro, from_= 0 , to= 100)
sp.pack()

sp1 = Spinbox(pro, from_= 20 , to= 40)
sp1.pack()
# Start the main event loop, allowing the GUI to be displayed and interacted with
pro.mainloop()