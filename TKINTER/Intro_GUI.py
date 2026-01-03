import tkinter as tk
from tkinter import font  # For making custom fonts importing font

# Used to create gui application using python
# Tk is a class

window = tk.Tk()    # This will create a window object
window.title("My application")   #Adding title
window.minsize(width=400, height=300)  # Size in pixels
                                              
# custom_font = tk.font.Font(family="Times New Roman", size=15, weight='bold', )
                                            #  Changing font style
label = tk.Label(text="Hello World!", font=("Times New Roman", 20, "bold"))  # Creating label
label.pack(expand="True")     # to make font place in center              # Using label class using pack() method  to put elements on the window   
label.config(font=("Courier New" ,25,))  # For cofiguration of font

window.mainloop()    # To get the window running on the screen 
# label.pack(side="right")     # position using side