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

hist = pd.read_csv("usdt.csv", usecols =[0,1,2,3,4],names=['time', 'low', 'high', 'open', 'close',])
hist = hist.set_index('time')
hist.index = pd.to_datetime(hist.index)
hist=hist.reindex(index=hist.index[::-1])
hist.head()


from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, LSTM
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_absolute_error
from keras.models import load_model



################################ TKINTER GUI ##################################

root = Tk()



#label_1 = Label(root, text="File name:")
#entry_1 = Entry(root)
#entry_1.insert(0,"Input")
#label_1.grid(sticky=E)
#entry_1.grid(row=0, column=1, columnspan=3)
a=Entry(root)
a.grid(sticky="W",row=0,column=1)


target_col = 'close'
def train_test_split(df, test_size=0.05):
    split_row = len(df) - int(test_size * len(df))
    split=1622
    train_data = df.iloc[:split_row]
    test_data = df.iloc[split_row:]
    say_test_data=df.iloc[987:]
    print('split',split_row)
    return train_data, test_data,say_test_data
train, test,say_test = train_test_split(hist, test_size=0.1)

testnew=hist.iloc[1022:]
print('sai',len(hist))
testadd=11

def line_plot(line1, line2, label1=None, label2=None, title='', lw=2):
    fig, ax = plt.subplots(1, figsize=(16, 9))
    ax.plot(line1, label=label1, linewidth=lw)
    ax.plot(line2, label=label2, linewidth=lw)
    ax.set_ylabel('price [USD]', fontsize=14)
    ax.set_title(title, fontsize=18)
    ax.legend(loc='best', fontsize=18);

def single_plot(line1, label1=None, title='', lw=2):
    fig, ax = plt.subplots(1, figsize=(16, 9))
    ax.plot(line1, label=label1, linewidth=lw)
    ax.set_ylabel('price [USD]', fontsize=14)
    ax.set_title(title, fontsize=18)
    ax.legend(loc='best', fontsize=18);
    
    
    
    

plt.show()
def normalise_zero_base(df):
    return df / df.iloc[0] - 1

def normalise_min_max(df):
    return (df - df.min()) / (data.max() - df.min())

def extract_window_data(df, window_len=10, zero_base=True):
 
    window_data = []
    for idx in range(len(df) - window_len):
        tmp = df[idx: (idx + window_len)].copy()
        if zero_base:
            tmp = normalise_zero_base(tmp)
        window_data.append(tmp.values)
    return np.array(window_data)

def prepare_data(df, target_col, window_len=10, zero_base=True, test_size=0.2):
    """ Prepare data for LSTM. """
    # train test split
    train_data, test_data,say_test_data = train_test_split(df, test_size=test_size)
    
    # extract window data
    X_train = extract_window_data(train_data, window_len, zero_base)
    X_test = extract_window_data(test_data, window_len, zero_base)
    
    # extract targets
    y_train = train_data[target_col][window_len:].values
    y_test = test_data[target_col][window_len:].values
    if zero_base:
        y_train = y_train / train_data[target_col][:-window_len].values - 1
        y_test = y_test / test_data[target_col][:-window_len].values - 1

    return train_data, test_data, X_train, X_test, y_train, y_test



print(test.size)
def build_lstm_model(input_data, output_size, neurons=20, activ_func='linear',
                     dropout=0.25, loss='mae', optimizer='adam'):
    model = Sequential()

    model.add(LSTM(neurons, input_shape=(input_data.shape[1], input_data.shape[2])))
    model.add(Dropout(dropout))
    model.add(Dense(units=output_size))
    model.add(Activation(activ_func))

    model.compile(loss=loss, optimizer=optimizer)
    return model

np.random.seed(42)

# data params
window_len = 7
test_size = 0.1
zero_base = True

# model params
lstm_neurons = 20
epochs = 5
batch_size = 4
loss = 'mae'
dropout = 0.25
optimizer = 'adam'

train, test, X_train, X_test, y_train, y_test = prepare_data(hist, target_col, window_len=window_len, zero_base=zero_base, test_size=test_size)
#say_test_data.head()

model = load_model('modelusdt.h5')
history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1, shuffle=True)

targets = test[target_col][window_len:]
preds = model.predict(X_test).squeeze()
mean_absolute_error(preds, y_test)

preds = test[target_col].values[:-window_len] * (preds + 1)
preds = pd.Series(index=targets.index, data=preds)

#line_plot(targets, preds, 'actual', 'prediction', lw=3)

#plt.show()


def saveentry():
    plt.close()
    name1 = a.get()
    start=len(preds)-120
    if int(name1)>4 and int(name1)<121:
        end=start+int(name1)
        single_plot(preds[start:end], 'Prediction', 'prediction', lw=3)
    else:
        messagebox.showerror("Error", "Enter Valid Details")
            
    
    #line_plot(train[target_col], test[target_col], 'training', 'test', title='BTC')

     
    plt.show()
def d7 ():
        plt.close()
        #plt.plot(train['low'], 'g', label = 'Low price')
        #plt.plot(train['high'], 'b', label = 'High price')
       # plt.plot(preds, 'g', label = 'Preds')
        #n=len(hist)-7
        #plt.plot(hist[target_col][n:], 'r', label = 'Closing price')
       # plt.legend(loc = 'upper right')
        single_plot(preds, 'prediction', 'prediction', lw=3)
        line_plot(targets, preds, 'actual', 'prediction', lw=3)
        plt.show()


#Button_1 = Button(root, text="Submit", command=saveentry)
#Button_1.grid(row=7,column=0, sticky=E)
Button(root, text="Submit",anchor="w",font=("Times", 10, "bold"),padx=15,command=saveentry).grid(sticky="W",row=0,column=2)
#a=Entry(root).grid(sticky="W",row=0,column=1)


root.mainloop()

# END OF SCRIPT
