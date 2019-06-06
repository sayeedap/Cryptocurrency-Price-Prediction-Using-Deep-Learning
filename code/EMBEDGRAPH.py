
import numpy as np

import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import pandas as pd
hist = pd.read_csv("ltcusd.csv", usecols =[0,1,2,3,4],names=['time', 'low', 'high', 'open', 'close',])
hist = hist.set_index('time')
hist.index = pd.to_datetime(hist.index)
hist=hist.reindex(index=hist.index[::-1])
target_col = 'close'
def train_test_split(df, test_size=0.05):
    split_row = len(df) - int(test_size * len(df))
    train_data = df.iloc[:split_row]
    test_data = df.iloc[split_row:]
    say_test_data=df.iloc[987:]
    print(split_row)
    return train_data, test_data,say_test_data
def line_plot(line1, line2, label1=None, label2=None, title='', lw=2):
    fig, ax = plt.subplots(1, figsize=(16, 9))
    ax.plot(line1, label=label1, linewidth=lw)
    ax.plot(line2, label=label2, linewidth=lw)
    ax.set_ylabel('price [USD]', fontsize=14)
    ax.set_title(title, fontsize=18)
    ax.legend(loc='best', fontsize=18);





class mclass:
    def __init__(self,  window):
        self.window = window
        #self.box = Entry(window)
        #self.button = Button (window, text="check", command=self.plot)
        
        #self.button1 = Button (window, text="check", command=self.d7)
        
        #self.button2 = Button (window, text="check", command=self.m3)
        def train_test_split(df, test_size=0.05):
            split_row = len(df) - int(test_size * len(df))
            train_data = df.iloc[:split_row]
            test_data = df.iloc[split_row:]
            say_test_data=df.iloc[987:]
            print(split_row)
            return train_data, test_data,say_test_data
        train, test,say_test = train_test_split(hist, test_size=0.1)
        Button(window, text="7d",anchor="w",font=("Times", 15, "bold"),pady=15,command=self.d7).grid(sticky="W",row=0,column=1)
        Button(window, text="1m",anchor="w",font=("Times", 15, "bold"),pady=15,command=self.d7).grid(sticky="W",row=0,column=2)
        Button(window, text="3m",anchor="w",font=("Times", 15, "bold"),pady=15,command=self.m3).grid(sticky="W",row=0,column=3)
        Button(window, text="1y",anchor="w",font=("Times", 15, "bold"),pady=15,command=self.y1).grid(sticky="W",row=0,column=4)
        Button(window, text="All",anchor="w",font=("Times", 15, "bold"),pady=15,command=self.all).grid(sticky="W",row=0,column=5)

        
        #self.button = Button (window, text="check", command=self.plot)
        #self.box.pack ()
        #self.button.pack()
        #self.button1.pack()
        #self.button2.pack()

    def plot (self):
        # x axis values
        
        train, test,say_test = train_test_split(hist, test_size=0.1)
        line_plot(train[target_col], test[target_col], 'training', 'test', title='BTC')

        
    def d7 (self):
        line_plot(train[target_col], test[target_col], 'training', 'test', title='BTC')
        plt.show()
        
    def m3 (self):
        pass
    def y1 (self):
        pass
        
    def all (self):
        pass
        

window= Tk()
start= mclass (window)
window.mainloop()
