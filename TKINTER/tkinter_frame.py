import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My application")

my_frame = ttk.Frame()
my_frame.pack(side="left", fill='both', expand=True)

label1 = tk.Label(my_frame, text="Hello World!", bg="red")
label1.pack(side="top", fill='both', expand=True)

label2 = tk.Label(text="How are you?", bg="blue")
label2.pack(side="top", fill='both', expand=True)

label3 = tk.Label(text="Have a nice day.", bg="green")
label3.pack(side="top", fill='both', expand=True)


window.mainloop()

# Fill makes the widget to glow to utilize the reserved space.
# vertical fill for red use y , both for both directions, x for horizontal direction.
# other component or labels are not affected by the fill property of 1 label.

# Frames gives a separate window inside the main window.
# To add the component of main window inside the frame, we need to use that frame as a first argument.

