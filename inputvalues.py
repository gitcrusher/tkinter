from tkinter import *

from jupyterlab.extensions import entry

root = Tk()

e = Entry(root, width=50, borderwidth=5, fg="white", bg = "black")
e.pack()
e.insert(0,"Enter your name ")

def myClick():
    hello = "Hello "+ e.get()
    myLabel = Label(root, text =hello)
    myLabel.pack()

myButton = Button(root, text= "Enter you text", command=myClick)
myButton.pack()

root.mainloop()