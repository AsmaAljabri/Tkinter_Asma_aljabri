from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB import database

db = database("Employee.DB")

# Create the main application window
root = Tk()
root.title('Employee Management System')
root.geometry('1250x615+0+0')  # Set the window size and position
root.resizable(False, False)  # Disable window resizing
root.configure(bg='#2c3e50')  # Set the background color

# Now you can define the Tkinter variables
name = StringVar()
age = StringVar()
Job = StringVar()
gender = StringVar()
Email = StringVar()
mobile = StringVar()


def getdata(event):
    selected_row =tv.focus()
    data = tv.item(selected_row)
    global row 
    row = data['values']
    name.set(row[1])
    age.set(row[2])
    Job.set(row[3])
    Email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])
    textAddress.delete(1.0,END)
    textAddress.insert(END,row[7])

def delete():
    db.remove(row[0])
    clear()
    displayall()

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def clear():
    name.set("")
    age.set("")
    Job.set("")
    Email.set("")
    gender.set("")
    mobile.set("")
    textAddress.delete(1.0,END)

def add_employee():
    if textName.get() == "" or textAge.get() == "" or textJob.get() == "" or textEmail.get() == "" or textmobile.get() == "" or comboGender.get() == "" or textAddress.get(1.0,END) == "":
        messagebox.showerror("Error","Please Fill All the Entries")
        return
    
    db.insert(
        textName.get(),
        textAge.get(),
        textJob.get(),
        textEmail.get(),
        comboGender.get(),
        textmobile.get(),
        textAddress.get(1.0,END))
    messagebox.showinfo("Success","Added New Employee")
    clear()
    displayall()


def upate():
    if textName.get() == "" or textAge.get() == "" or textJob.get() == "" or textEmail.get() == "" or textmobile.get() == "" or comboGender.get() == "" or textAddress.get(1.0,END) == "":
        messagebox.showerror("Error","Please Fill All the Entries")
        return
    db.update(row[0],
        textName.get(),
        textAge.get(),
        textJob.get(),
        textEmail.get(),
        comboGender.get(),
        textmobile.get(),
        textAddress.get(1.0,END)
    )
    messagebox.showinfo("Success","The Employee Data is Updated")
    clear()
    displayall()
   
    



# ======================Entry frame =======================
# Create a frame for input entries
entries_frame = Frame(root, bg='#2c3e50')
entries_frame.place(x=1, y=1, width=360, height=510)

# Create a title label
title = Label(entries_frame, text='Employee Details', font=('Calibri', 18, 'bold'), bg='#2c3e50', fg='white')
title.place(x=1, y=1)

# Create labels and entry fields for employee information
labName = Label(entries_frame, text="Name", font=('Calibri', 16), bg='#2c3e50', fg='white')
labName.place(x=10, y=50)

textName = Entry(entries_frame,textvariable = name ,width=20, font=('Calibri', 16))
textName.place(x=120, y=50)

labJob = Label(entries_frame, text="Job", font=('Calibri', 16), bg='#2c3e50', fg='white')
labJob.place(x=10, y=90)

textJob = Entry(entries_frame, textvariable = Job,width=20, font=('Calibri', 16))
textJob.place(x=120, y=90)

labGender = Label(entries_frame, text="Gender", font=('Calibri', 16), bg='#2c3e50', fg='white')
labGender.place(x=10, y=130)

# Create a dropdown (combo box) for gender selection
comboGender = ttk.Combobox(entries_frame, textvariable = gender,state='readonly', width=18, font=('Calibri', 16))
comboGender['values'] = ("Male", "Female")
comboGender.place(x=120, y=130)

labAge = Label(entries_frame, text="Age", font=('Calibri', 16), bg='#2c3e50', fg='white')
labAge.place(x=10, y=170)

textAge = Entry(entries_frame, textvariable =age,width=20, font=('Calibri', 16))
textAge.place(x=120, y=170)

labEmail = Label(entries_frame, text="Email", font=('Calibri', 16), bg='#2c3e50', fg='white')
labEmail.place(x=10, y=210)

textEmail = Entry(entries_frame,textvariable =Email, width=20, font=('Calibri', 16))
textEmail.place(x=120, y=210)

labContact = Label(entries_frame, text="Contact", font=('Calibri', 16), bg='#2c3e50', fg='white')
labContact.place(x=10, y=250)

textmobile = Entry(entries_frame, textvariable =mobile,width=20, font=('Calibri', 16))
textmobile.place(x=120, y=250)

labAddress = Label(entries_frame, text="Address", font=('Calibri', 16), bg='#2c3e50', fg='white')
labAddress.place(x=10, y=290)

# Create a text field for the address
textAddress = Text(entries_frame, width=30, height=2, font=('Calibri', 16))
textAddress.place(x=10, y=330)

        
logo = PhotoImage(file='logo3.png')
lab_logo  = Label(root,image= logo, bg='#2c3e50')
lab_logo.place(x= 120, y=510)


#========================= buttons frame =======================

btn_frame = Frame(entries_frame, bg='#2c3e50', bd=1, relief=SOLID)
btn_frame.place(x=10, y=400, width=330, height=100)

btnadd = Button(btn_frame,
                text='Add Details',
                width=14, height=1,
                font=('Calibri', 16),
                fg='white',
                bg='#16a085',
                bd=0,
                command= add_employee)
btnadd.place(x=4, y=5)

btnupd = Button(btn_frame,
                text='Update Details',
                width=14, height=1,
                font=('Calibri', 16),
                fg='white',
                bg='#2980b9',
                bd=0,
                command=upate)
btnupd.place(x=4, y=50)

btndel = Button(btn_frame,
                text='Delete Details',
                width=13, height=1,
                font=('Calibri', 16),
                fg='white',
                bg='#c0392b',
                command=delete,
                bd=0)
btndel.place(x=170, y=5)

btnclear = Button(btn_frame,
                  text='Clear Details',
                  width=13, height=1,
                  font=('Calibri', 16),
                  fg='white',
                  bg='#f39c12',
                  command= clear,
                  bd=0)
btnclear.place(x=170, y=50)
# ============================hide and show buttom [define]=============

def hide():
    root.geometry("365x615+0+0")

def show():
    root.geometry('1250x615+0+0')  

btnhide =Button(entries_frame,text = "HIDE",cursor='hand2',bg ='white',bd = 1,relief=GROOVE , command= hide)
btnhide.place(x=270, y=10)

btnshow =Button(entries_frame,text = "SHOW",cursor='hand2',bg ='white',bd = 1,relief=GROOVE, command= show)
btnshow.place(x=310, y=10)

# ===================== Data Table Frame =========
tree_frame = Frame(root, bg='white')
tree_frame.place(x=365, y=1, width=882, height=610)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 13), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13))

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("#1", text="ID")
tv.column("#1", width=40)

tv.heading("#2", text="Name")
tv.column("#2", width=140)

tv.heading("#3", text="Age")
tv.column("#3", width=50)

tv.heading("#4", text="Job")
tv.column("#4", width=120)

tv.heading("#5", text="Email")
tv.column("#5", width=150)

tv.heading("#6", text="Gender")
tv.column("#6", width=90)

tv.heading("#7", text="Mobile")
tv.column("#7", width=150)

tv.heading("#8", text="Address")
tv.column("#8", width=190)

tv['show'] = 'headings'
tv.place(x=1,y=1,height=610)
tv.bind("<ButtonRelease-1>",getdata)



displayall()

# Start the main GUI event loop
root.mainloop()
