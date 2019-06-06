from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from math import cos, sin
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


################################ TKINTER GUI ##################################

root = Tk()



#label_1 = Label(root, text="File name:")
#entry_1 = Entry(root)
#entry_1.insert(0,"Input")
#label_1.grid(sticky=E)
#entry_1.grid(row=0, column=1, columnspan=3)


hist = pd.read_csv("lttcc.csv", usecols =[0,1,2,3,4],names=['time', 'low', 'high', 'open', 'close',])
hist = hist.set_index('time')
hist.index = pd.to_datetime(hist.index)
hist=hist.reindex(index=hist.index[::-1])
target_col = 'close'
def train_test_split(df, test_size=0.05):
    split_row = len(df) - int(test_size * len(df))
    train_data = df.iloc[:split_row]
    test_data = df.iloc[split_row:]
    say_test_data=df.iloc[987:]
    print(len(hist))
    return train_data, test_data,say_test_data
def line_plot(line1, line2, label1=None, label2=None, title='', lw=2):
    fig, ax = plt.subplots(1, figsize=(16, 9))
    ax.plot(line1, label=label1, linewidth=lw)
    ax.plot(line2, label=label2, linewidth=lw)
    ax.set_ylabel('price [USD]', fontsize=14)
    ax.set_title(title, fontsize=18)
    ax.legend(loc='best', fontsize=18);

train, test,say_test = train_test_split(hist, test_size=0.1)




def saveentry():
    plt.close()
    name1 = entry_1.get()

################################### PLOTTING ##################################
    
    line_plot(train[target_col], test[target_col], 'training', 'test', title='BTC')

     
    plt.show()
def d7 ():
        plt.close()
        #plt.plot(train['low'], 'g', label = 'Low price')
        #plt.plot(train['high'], 'b', label = 'High price')
        #plt.plot(train['open'], 'g', label = 'Opening price')
        n=len(hist)-7
        print(n)
        plt.plot(hist[target_col][854:861], 'r', label = 'Closing price')
        plt.legend(loc = 'upper right')
        plt.xlabel('Days') 
        # naming the y axis 
        plt.ylabel('price(USD)') 
        
        
        plt.title('7d Chart')
        plt.show()
def m1 ():
        plt.close()
        #plt.plot(train['low'], 'g', label = 'Low price')
        #plt.plot(train['high'], 'b', label = 'High price')
        #plt.plot(train['open'], 'g', label = 'Opening price')
        n=len(hist)-31-75
        plt.plot(hist[target_col][n:861], 'r', label = 'Closing price')
        plt.legend(loc = 'upper right')
        plt.xlabel('Days') 
        # naming the y axis 
        plt.ylabel('price(USD)') 
        
        plt.title('1m Chart')
        plt.show()
        
def m3 ():
        plt.close()
        #plt.plot(train['low'], 'g', label = 'Low price')
        #plt.plot(train['high'], 'b', label = 'High price')
        #plt.plot(train['open'], 'g', label = 'Opening price')
        n=len(hist)-93-75
        plt.plot(hist[target_col][n:861], 'r', label = 'Closing price')
        plt.legend(loc = 'upper right')
        plt.xlabel('Days') 
        # naming the y axis 
        plt.ylabel('price(USD)') 
        
        
        plt.title('3m Chart')
        plt.show()
def y1 ():
        plt.close()
        n=len(hist)-365-75
        plt.plot(hist[target_col][n:861], 'r', label = 'Closing price')
        plt.legend(loc = 'upper right')
        plt.xlabel('Days') 
        # naming the y axis 
        plt.ylabel('price(USD)')
        
        plt.title('1y Chart')
        
        plt.show()
        
        
def all ():
        plt.close()
        plt.plot(hist[target_col], 'r', label = 'Closing price')
        plt.legend(loc = 'upper right')
        plt.xlabel('Days') 
        # naming the y axis 
        plt.ylabel('price(USD)') 
        
        plt.title('All Chart')
        plt.show()
        

#Button_1 = Button(root, text="Submit", command=saveentry)
#Button_1.grid(row=7,column=0, sticky=E)
Button(root, text="7d",anchor="w",font=("Times", 10, "bold"),padx=15,command=d7).grid(sticky="W",row=0,column=1)
Button(root, text="1m",anchor="w",font=("Times", 10, "bold"),padx=15,command=m1).grid(sticky="W",row=0,column=2)
Button(root, text="3m",anchor="w",font=("Times", 10, "bold"),padx=15,command=m3).grid(sticky="W",row=0,column=3)
Button(root, text="1y",anchor="w",font=("Times", 10, "bold"),padx=15,command=y1).grid(sticky="W",row=0,column=4)
Button(root, text="All",anchor="w",font=("Times", 10, "bold"),padx=15,command=all).grid(sticky="W",row=0,column=5)


root.mainloop()

# END OF SCRIPT
