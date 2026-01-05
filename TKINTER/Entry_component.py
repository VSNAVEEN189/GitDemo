import tkinter as tk
import tkinter.font as font 
from tkinter import Entry


window = tk.Tk()   
window.title("My application")   
window.minsize(width=400, height=300)  

custom_font = tk.font.Font(family="Times New Roman", size=20, weight='bold', )

label = tk.Label(text="Hello World!", font=custom_font) 
label.pack()                

label["text"] = "Have a nice day!"
label.config(text="My new app")

def function_button():
    input_text = user_input.get()
    label.config(text=input_text)   

# Taking user input using Entry 
user_input = tk.Entry(width=30)
user_input.pack()
print(user_input.get())

# Button
button = tk.Button(text="Click", command=function_button)
button.pack()

window.mainloop()    
