# Create a Window Resizer GUI using Tkinter in Python


# Hints
# Create a GUI window that takes the input of width and height
# Create a Button "Apply" and after clicking on this button it will change the size of the GUI window accordingly
# Code as described/written in the video


from tkinter import *


root = Tk()
root.title("Window Resize")
root.geometry("600x600")

def apply_getval():
    height= heightvalue.get()
    width = widthvalue.get()
    root.geometry(f"{width}x{height}")


Label(root,text= "Width", font= "Lucida 13 bold").grid(row=0,column=1)
Label(root, text = "Height", font= "Lucida 13 bold").grid(row=1,column=1)

widthvalue = StringVar()
heightvalue = StringVar()

Entry(root, textvariable= widthvalue).grid(row=0 , column=2)
Entry(root, textvariable= heightvalue).grid(row= 1, column=2)



Button(text= "Apply" , command= apply_getval, font= "Lucida 10 bold").grid( column=2)

root.mainloop()