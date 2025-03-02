from tkinter import *

root = Tk()

def myClick():
    label1 = Label(root,text="Look! I clicked!!")
    label1.pack()
#state is disabled no enabled
#padx and pad ya re also some paramaterized fuction inside this widget
#to make it run the function add command argument as well
#fg = foreground color , bg = background color
myButton = Button(root , text="Click me!", padx= 50 , pady=25, command= myClick , fg="blue", bg="red")
myButton.pack()
root.mainloop()