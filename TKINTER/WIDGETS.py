import tkinter as tk
import tkinter.font as font 
from tkinter import Entry
from tkinter import ttk

window = tk.Tk()   
window.title("My application")   
window.minsize(width=400, height=300)  

custom_font = tk.font.Font(family="Times New Roman", size=20, weight='bold', )

label = ttk.Label(text="Hello World!", font=custom_font, padding=15) 
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
quit_button.pack(pady=12)  

# SEPARATOR WIDGET
sep = ttk.Separator(orient='horizontal')
sep.pack(fill='x')

# TEXT WIDGET
# For height and width of text widget
text = tk.Text(height=5, width=25)
text.pack(pady=10)
#  for cursor to blink inside the text widget
text.focus()
# Insert method default text
text.insert("1.0", "Enter your comments")  

text_data = text.get("1.0", "end")

def text_function():
    text_data = text.get("1.0", "end")
    print(text_data)

text_button = ttk.Button(text="Get Text", command=text_function)
text_button.pack()
# Created a button to see text in the console

# To disable the widget
# text["state"] = "disabled"

# def enable_text():
#     text["state"] = "normal"

# enable_button = ttk.Button(text="Enable text box", command=enable_text)
# enable_button.pack()

check_option = tk.StringVar()

def check_option_task():
    print(check_option.get(), type(check_option.get()))   

check_button = ttk.Checkbutton(text="Agree with terms and conditions?", variable=check_option, 
                               command=check_option_task, onvalue="Yes", offvalue="No")
check_button.pack()

# RADIO BUTTON WIDGET
radio_value = tk.StringVar()

def get_radio_value():
    print(radio_value.get())

option_1= ttk.Radiobutton(text="Male", variable=radio_value, value="male", command=get_radio_value)
option_2= ttk.Radiobutton(text="Female", variable=radio_value, value="female", command=get_radio_value)
option_1.pack()
option_2.pack()

# Combobox
selected_country = tk.StringVar()
country_box = ttk.Combobox(textvariable=selected_country, values=["India", "USA", "Australia", "Sweden", "Canada"])
country_box["state"] = "readonly"  # User can't enter their own value
country_box.pack()

def display_country(event):
    msg = f"Selected country is : {selected_country.get()}"
    country_label = ttk.Label(text=selected_country.get()) 
    country_label.pack()  
    # print(f"Selected country is : {selected_country.get()}")

country_box.bind("<<ComboboxSelected>>", display_country)

# Listbox
food_items = ["Pizza", "Burger", "Garlic bread", "Nachos", "Salad"]
fav_food = tk.StringVar(value=food_items)

food_list=tk.Listbox(listvariable=fav_food, height=5, selectmode="extended")  #selectmode can choose multiple options
food_list.pack()

def get_fav_food(event):
    food_indices = food_list.curselection()  # returns tuple of indices of selected items
    for i in food_indices:
        print(food_list.get(i))

food_list.bind("<<ListboxSelect>>", get_fav_food)

#Spinbox - It's like a counter with up and down arrows 
counter = tk.IntVar(value=10)

def get_spin_box_value():
    print(f"Current spinbox value: {spin_box.get()}")

spin_box = ttk.Spinbox(values=tuple(range(0, 105, 5)), textvariable=counter, wrap=True, command=get_spin_box_value)
spin_box.pack()

print(f"Initial spinbox value: {spin_box.get()}")  #To get the current value of spinbox to get each time we have to create a function 

window.mainloop()    

# padding=15 Wont't work for button
# checkbutton is combinaton of button and label
# Class for tkinter integer IntVar, for string values StringVar. to add some values after clicking checkbox onvalue="Yes", offvalue="No"
# Radio buttons are used in forms

# combobox, readonly created an event using bind method
# string var should not be assigned to listbox using textvariable, use listvariable instead
# Both of them uses bind method to trigger an event and get selected items
# wrap in spinbox makes the value to start from beginning when it reaches the max values