from tkinter import * 

# Create the main window
pro = Tk()
pro.geometry("800x500")

# Create the first frame
frame1 = Frame(width='390', height='497', bg='blue')
frame1.place(x=1, y=1)
# The above lines create a Frame widget named 'frame1' with a width of 390 pixels,
# height of 497 pixels, and a background color of blue. The place() method is used
# to position the frame at coordinates (1, 1) within the main window.

# Create the second frame
frame2 = Frame(width='390', height='497', bg='green')
frame2.place(x=395, y=1)
# Similarly, this creates another Frame widget named 'frame2' with the same dimensions
# but with a background color of green. It's placed at coordinates (395, 1) within
# the main window.

# Adding buttons to the frames
# The following lines create Button widgets within the respective frames.
# The buttons are placed at coordinates (10, 10) within their frames.
# The fg parameter specifies the foreground (text) color, and bg specifies the background color.
bt1_frame1 = Button(frame1, text='button1', fg='black', bg='white', width='20')
bt1_frame1.place(x=10, y=10) 

bt1_frame2 = Button(frame2, text='button2', fg='red', bg='black', cursor='star', width='20')
bt1_frame2.place(x=10, y=10)  

# Adding labels to the frames
# The following lines create Label widgets within the respective frames.
# The labels display instructions for each button.
Label1 = Label(frame1, text='Select the first button', fg='white', bg='blue', font=12)
Label1.place(x=10, y=40)

Label2 = Label(frame2, text='Select the second button', fg='black', bg='green', font=12)
Label2.place(x=10, y=40)

# Adding Entry widgets to the frames
# Entry widgets are used to accept user input.
# The following lines create Entry widgets within the respective frames.
en1 = Entry(frame1)
en1.place(x=10, y=70)  
# This Entry widget allows users to input text. It's placed at coordinates (10, 70) within frame1.

en2 = Entry(frame1, justify="center", fg="red", bg="black")
en2.place(x=10, y=90)  
# Here, we've customized this Entry widget to have centered text, red foreground color,
# and a black background. It's placed at coordinates (10, 90) within frame1.

en3 = Entry(frame1, justify="center", fg="red", bg="black", font=14)
en3.place(x=10, y=120)  
# This Entry widget combines the customizations of centered text, red foreground color,
# black background, and a larger font size (14). It's placed at coordinates (10, 120) within frame1.

en4 = Entry(frame2)
en4.place(x=10, y=70)  
# Similar to en1, this Entry widget allows users to input text and is placed at coordinates (10, 70) within frame2.

en5 = Entry(frame2, justify="center", fg="red", bg="black")
en5.place(x=10, y=90)  
# This Entry widget in frame2 is customized with centered text, red foreground color,
# and a black background. It's placed at coordinates (10, 90) within frame2.

en6 = Entry(frame2, justify="center", fg="red", bg="black", font=14)
en6.place(x=10, y=120)  
# This Entry widget in frame2 combines the customizations of centered text, red foreground color,
# black background, and a larger font size (14). It's placed at coordinates (10, 120) within frame2.

pro.mainloop()
# The main event loop is started, allowing the GUI to be displayed and interacted with.
