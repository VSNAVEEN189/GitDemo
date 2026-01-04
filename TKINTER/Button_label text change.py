import tkinter as tk
import tkinter.font as font 


window = tk.Tk()   
window.title("My application")   
window.minsize(width=400, height=300)  

custom_font = tk.font.Font(family="Times New Roman", size=20, weight='bold', )

label = tk.Label(text="Hello World!", font=custom_font) 
label.pack()                
# label.config(font=("Courier New" ,25,))  

# Changing text of the label 2 methods.
label["text"] = "Have a nice day!"
label.config(text="My new app")

counter = 0
def function_button():
    global counter        # global
    counter += 1          #Gets to know how many times button got clicked 
    label.config(text=f"The button got clicked! {counter} times")   

# Button
button = tk.Button(text="Click", command=function_button)
button.pack()

window.mainloop()    
