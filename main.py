# import tkinter as tk
# from tkinter import PhotoImage

# def menu_button_clicked():
#     print("Menu button clicked")

# # Create the main window
# root = tk.Tk()

# # Load the image
# image = PhotoImage(file="downarrow.png")  # Replace "image.png" with the path to your image file

# # Create the menu button
# menu_button = tk.Button(root, text="Button Text", image=image, compound="left", command=menu_button_clicked,height=50,width=100)
# menu_button.pack()

# # Run the application
# root.mainloop()

# from tkinter import *      
# a= Tk()  
# a.geometry("400x400")  
# frame1=Frame(a,bg = "green",bd=10,width=100,  
#              height=50,cursor = "  hand1 ").pack(side=TOP)  
# frame2=Frame(a,bg = "red",width=100,  
#              height=50,cursor = "man").pack(side=RIGHT)  
# frame3=Frame(a,bg = "yellow",bd=10,width=100,  
#              height=50,cursor = "target").pack(side=LEFT)  
# frame4=Frame(a,bg = "blue",bd=10,width=100,  
#              height=50,cursor = "target").pack(side=BOTTOM)  
# a.mainloop()  
# Output    

# from tkinter import *

# #Create an instance of Tkinter Frame
# win = Tk()

# #Set the geometry of window
# win.geometry("700x350")

# #Add a background color to the Main Window
# win.config(bg = '#add123')

# #Create a transparent window
# win.wm_attributes('-transparentcolor','#add123')
# win.mainloop()

# Import module
# from tkinter import *
 
# # Create object
# root = Tk()
 
# # Adjust size
# root.geometry("400x400")
 
# # Create transparent window
# root.attributes('-alpha',0.5)
 
# # Execute tkinter
# root.mainloop()

import tkinter as tk
import tkinter.ttk as ttk
 
root = tk.Tk()
 
ttk.Button(root, text='Text').grid(row=0, column=0)
ttk.Button(root, text='Text', padding=5).grid(row=1, column=0)
ttk.Button(root, text='Text', padding=-5).grid(row=2, column=0)
ttk.Button(root, text='Text', width=4).grid(row=3, column=0)
 
tk.mainloop()