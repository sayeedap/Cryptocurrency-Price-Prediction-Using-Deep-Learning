from tkinter import *
import tkinter as tk
import os


def donothing():
    root.destroy()
    os.system('conv\convert.py')
   
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Currency Exchange", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)





root.config(menu=menubar)
root.mainloop()
