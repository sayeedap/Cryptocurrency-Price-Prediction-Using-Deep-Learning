from tkinter import *
import tkinter as tk
from tkinter import font
import requests

##graph
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os

#graphclose

price_api_url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,XLM,LTC,USDT,XMR&tsyms=USD'
response_price= requests.get(price_api_url)
response_json = response_price.json()
#type(response_json) # The API returns a list

# Bitcoin data is the first element of the list
bitcoinprice=response_json['BTC']['USD']


 
window = Tk()


window.geometry('1200x700')


window.title("Crypto currency")
def donothing():
    window.destroy()
    os.system('convert.py')
   

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Currency Exchange", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

window.config(menu=menubar)



m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
m2 = PanedWindow(m1, orient=VERTICAL,height=50,handlesize=0)
m1.add(m2)

top = Label(m2,bg='#3b5998' ,fg='white',justify=LEFT,text="Cryptocurrency Price Predictor",height=3,font=("Times", 20, "bold"),pady=20,padx=0,bd=0)
m2.add(top)
m3 = PanedWindow(m2)
m2.add(m3)

logobtc = tk.PhotoImage(file='btc.png')
logoeth = tk.PhotoImage(file='ethe.png')
logoxrp = tk.PhotoImage(file='xrp.png')
logoxlm = tk.PhotoImage(file='xlm.png')
logoltc = tk.PhotoImage(file='ltc.png')
logousdt = tk.PhotoImage(file='usdt.png')
logoxmr = tk.PhotoImage(file='xmr.png')


def graphbtc():
        os.system('pre_btc1.py')
def grapheth():
        os.system('pre_eth1.py')
def graphxrp():
        os.system('pre_xrp1.py')
def graphbch():
        os.system('pre_xlm1.py')
def graphltc():
        os.system('pre_ltc1.py')
def graphada():
        os.system('pre_usdt1.py')
        
def graphxmr():
        os.system('pre_xmr1.py')



Label(m3, text="#",anchor="w",font=("Times", 17, "bold",'underline'),pady=15).grid(row=0,column=0,columnspan=3)

Label(m3, text="Name",anchor="w",font=("Times", 17, "bold",'underline'),pady=15).grid(sticky="W",row=0,column=4)
Label(m3, text="Price",anchor="w",font=("Times", 17, "bold",'underline'),pady=15).grid(sticky="W",row=0,column=6)

Label(m3, text="1",anchor="w",font=("Times", 15, "bold")).grid(sticky="W",row=3,column=0)
Label(m3, text="    ",font=("Times", 15, "bold")).grid(sticky="W",row=3,column=1)
Label(m3,image=logobtc).grid(sticky="W",row=3,column=2)
#Label(m3, text="    ",font=("Times", 15, "bold")).grid(sticky="W",row=0,column=1)
Label(m3, text="    ",font=("Times", 15, "bold")).grid(sticky="W",row=3,column=3)

Label(m3, text="    ",font=("Times", 15, "bold")).grid(sticky="W",row=3,column=7)

Label(m3, text="    ",font=("Times", 15, "bold")).grid(sticky="W",row=3,column=9)
a=Label(m3, text="Bitcoin (BTC)",anchor="w",font=("Times", 15, "bold"),pady=15).grid(sticky="W",row=3,column=4)


Button(m3, text="Prediction",anchor="w",font=("Times", 10, "bold"),padx=15,command=graphbtc).grid(sticky="W",row=3,column=10)

Label(m3, text="  ",font=("Times", 15, "bold")).grid(sticky="W",row=3,column=5)
Label(m3, text=response_json['BTC']['USD'],font=("Times", 15, "bold")).grid(sticky="W",row=3,column=6)



Label(m3, text="2",anchor="w",font=("Times", 15, "bold"),pady=15).grid(sticky="W",row=4,column=0)
Label(m3,image=logoeth).grid(sticky="W",row=4,column=2)
Label(m3, text="Ethereum (ETH)",justify=LEFT,font=("Times", 15, "bold")).grid(sticky="W",row=4,column=4)
Label(m3, text=response_json['ETH']['USD'],font=("Times", 15, "bold")).grid(sticky="W",row=4,column=6)
Button(m3, text="Prediction",anchor="w",font=("Times", 10, "bold"),padx=15,command=grapheth).grid(sticky="W",row=4,column=10)

Label(m3, text="3",anchor="w",font=("Times", 15, "bold"),pady=15).grid(sticky="W",row=5,column=0)
Label(m3,image=logoxrp).grid(sticky="W",row=5,column=2)
Label(m3, text="Ripple (XRP)",justify=LEFT,font=("Times", 15, "bold")).grid(sticky="W",row=5,column=4)
Label(m3, text=response_json['XRP']['USD'],font=("Times", 15, "bold")).grid(sticky="W",row=5,column=6)
Button(m3, text="Prediction",anchor="w",font=("Times", 10, "bold"),padx=15,command=graphxrp).grid(sticky="W",row=5,column=10)

Label(m3, text="4",anchor="w",font=("Times", 15, "bold"),pady=15).grid(sticky="W",row=6,column=0)

Label(m3,image=logoxlm).grid(sticky="W",row=6,column=2)
Label(m3, text="Stellar (xlm)",justify=LEFT,font=("Times", 15, "bold")).grid(sticky="W",row=6,column=4)
Label(m3, text=response_json['XLM']['USD'],font=("Times", 15, "bold")).grid(sticky="W",row=6,column=6)


Button(m3, text="Prediction",anchor="w",font=("Times", 10, "bold"),padx=15,command=graphbch).grid(sticky="W",row=6,column=10)


Label(m3, text="5",anchor="w",font=("Times", 15, "bold"),pady=15).grid(sticky="W",row=7,column=0)
Label(m3,image=logoltc).grid(sticky="W",row=7,column=2)
Label(m3, text="Litecoin (LTC)",font=("Times", 15, "bold")).grid(sticky="W",row=7,column=4)
Label(m3, text=response_json['LTC']['USD'],font=("Times", 15, "bold")).grid(sticky="W",row=7,column=6)


Button(m3, text="Prediction",anchor="w",font=("Times", 10, "bold"),padx=15,command=graphltc).grid(sticky="W",row=7,column=10)

Label(m3, text="6",anchor="w",font=("Times", 15, "bold"),pady=15).grid(sticky="W",row=8,column=0)
Label(m3,image=logousdt).grid(sticky="W",row=8,column=2)
Label(m3, text="Tether  (USDT)",font=("Times", 15, "bold")).grid(sticky="W",row=8,column=4)
Label(m3, text=response_json['USDT']['USD'],font=("Times", 15, "bold")).grid(sticky="W",row=8,column=6)


Button(m3, text="Prediction",anchor="w",font=("Times", 10, "bold"),padx=15,command=graphada).grid(sticky="W",row=8,column=10)

Label(m3, text="7",anchor="w",font=("Times", 15, "bold"),pady=15).grid(sticky="W",row=9,column=0)
Label(m3,image=logoxmr).grid(sticky="W",row=9,column=2)
Label(m3, text="Monero (XMR)",font=("Times", 15, "bold")).grid(sticky="W",row=9,column=4)
Label(m3, text=response_json['XMR']['USD'],font=("Times", 15, "bold")).grid(sticky="W",row=9,column=6)


Button(m3, text="Prediction",anchor="w",font=("Times", 10, "bold"),padx=15,command=graphxmr).grid(sticky="W",row=9,column=10)

#.....#


##graph
#x=np.array ([1, 2, 3])
#v= np.array ([5,6,7])
#p= np.array ([2,3,4])

#fig = Figure(figsize=(6,2))
#a = fig.add_subplot(111)
#a.plot(p,x,color='blue')

#canvas = FigureCanvasTkAgg(fig, master=m3)
#canvas.get_tk_widget().grid(sticky="W",row=1,column=8)
#canvas.draw()
##graph close



#bottom = Label(m2,bg='yellow', text="bottom pane")
#m2.add(bottom)




window.mainloop()
