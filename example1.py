from tkinter import *

window = Tk()
window.geometry("350x200")
window.title("COMP1753 GUI")

def clicked():
    lbl.configure(text="Button was clicked!", fg="red")

btn = Button(window, text="Click Me", command=clicked)
#btn = Button(window, text="Click Me", bg="orange", fg="red")
btn.grid(column=1, row=0)

lbl = Label(window, text="Hello")
lbl.grid(column=2, row=0)

window.mainloop()