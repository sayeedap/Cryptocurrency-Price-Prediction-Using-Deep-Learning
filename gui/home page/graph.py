import matplotlib.pyplot as plt  # import plot functions
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *

################################ TKINTER GUI ##################################

root = Tk()

label_1 = Label(root, text="File name:")
entry_1 = Entry(root)
entry_1.insert(0,"Input")
label_1.grid(sticky=E)
entry_1.grid(row=0, column=1, columnspan=3)

def saveentry():
    plt.close()
    name1 = entry_1.get()

################################### PLOTTING ##################################

    fig = plt.figure()
    ax = fig.gca(projection='3d') 

    plt.show(fig)

Button_1 = Button(root, text="Submit", command=saveentry)
Button_1.grid(row=7,column=0, sticky=E)

root.mainloop()

# END OF SCRIPT
