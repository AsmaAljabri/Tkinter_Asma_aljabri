import tkinter as tk
from tkinter import ttk

# Function to add a task to the agenda
def add_task():
    task = entry_task.get()
    day = combo_day.get()
    time = combo_time.get()
    
    if task and day and time:
        agenda_list.insert("", "end", values=(day, time, task))
        entry_task.delete(0, "end")  
    else:
        status_label.config(text="Please fill in all fields.")

# Initialize the main window
root = tk.Tk()
root.title("Weekly Agenda")

# Set the background color to light blue
root.configure(bg="#E6F7FF")

# Create and configure the Treeview widget to display the agenda
agenda_list = ttk.Treeview(root, columns=("Day", "Time", "Task"), show="headings")
agenda_list.heading("Day", text="Day")
agenda_list.heading("Time", text="Time")
agenda_list.heading("Task", text="Task")
agenda_list.pack()

# Create labels, entry fields, and comboboxes for input
label_task = tk.Label(root, text="Task:")
entry_task = tk.Entry(root)
label_task.pack()
entry_task.pack()

label_day = tk.Label(root, text="Day:")
combo_day = ttk.Combobox(root, values=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
label_time = tk.Label(root, text="Time:")
combo_time = ttk.Combobox(root, values=("Morning", "Afternoon", "Evening"))
label_day.pack()
combo_day.pack()
label_time.pack()
combo_time.pack()

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create a status label
status_label = tk.Label(root, text="", fg="red")
status_label.pack()

# Start the Tkinter main loop
root.mainloop()
