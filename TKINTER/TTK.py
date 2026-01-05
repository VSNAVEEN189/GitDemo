import tkinter as tk
import tkinter.font as font 
from tkinter import Entry
from tkinter import ttk

window = tk.Tk()   
window.title("My application")   
window.minsize(width=400, height=300)  

custom_font = tk.font.Font(family="Times New Roman", size=20, weight='bold', )

label = ttk.Label(text="Hello World!", font=custom_font) 
label.pack()                

label["text"] = "Have a nice day!"
label.config(text="My new app")

def function_button():
    input_text = user_input.get()
    label.config(text=input_text)   

# Taking user input using Entry 
user_input = ttk.Entry(width=30)
user_input.pack()
print(user_input.get())

# Button
button = ttk.Button(text="Click", command=function_button)
button.pack()

# Quit button for destroying the window
quit_button = ttk.Button(text="Quit", command=window.destroy)
quit_button.pack()  

window.mainloop()    
