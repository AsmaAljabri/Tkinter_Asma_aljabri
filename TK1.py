from tkinter import * 
# Create the main window
pro = Tk()

# (4) Set the dimensions and position of the window
pro.geometry("300x500+500+100") # Width x Height + Left + Top

#cour(5)  # Allow the window to be resizable in both dimensions
pro.resizable(True, True)

# Set the title of the window
pro.title("PythonTKinter")


# Set the background color of the window
pro.config(background="blue")

# Set the window icon
# icon path C:\\Users\\TechSupp\\Desktop\\python.ico

pro.iconbitmap('C:\\Users\\TechSupp\\Desktop\\python.ico')
  
# Set the minimum size of the window
# pro.minsize(width,height)

pro.minsize(200,200)

# Set the maximum size of the window

pro.maxsize(400,400)



# Start the main event loop to run the application
pro.mainloop()