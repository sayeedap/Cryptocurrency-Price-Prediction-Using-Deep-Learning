from tkinter import *
import tkinter as tk
from tkinter import font
import requests
import os

##graph
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#graphclose

#price_api_url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,BCH,LTC,ADA,XMR&tsyms=USD'
#response_price= requests.get(price_api_url)
#response_json = response_price.json()
#type(response_json) # The API returns a list

# Bitcoin data is the first element of the list
#bitcoinprice=response_json['BTC']['USD']


 
window = Tk()


window.geometry('1200x700')


window.title("Crypto currency")
def donothing():
    window.destroy()
    os.system('crypto.py')
   

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Home", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

window.config(menu=menubar)


logoBTC = tk.PhotoImage(file='btc.png')
logoETH = tk.PhotoImage(file='ethe.png')
logoXRP = tk.PhotoImage(file='xrp.png')
logoXLM = tk.PhotoImage(file='xlm.png')
logoLTC = tk.PhotoImage(file='ltc.png')
logoUSDT = tk.PhotoImage(file='usdt.png')
logoXMR = tk.PhotoImage(file='xmr.png')

list=['USD','BTC','ETH','XRP','XLM','LTC','USDT','XMR']


m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
m2 = PanedWindow(m1, orient=VERTICAL,height=50,handlesize=0)
m1.add(m2)

top = Label(m2,bg='#3b5998' ,fg='white',justify=LEFT,text="Cryptocurrency Price Predictor",height=3,font=("Times", 20, "bold"),pady=20,padx=0,bd=0)
m2.add(top)
m3 = PanedWindow(m2)
m2.add(m3)
OPTIONS = [
"BTC",
"ETH",
"XRP",
"XLM",
"LTC",
"USDT",
"XMR"
] #etc
Label(m3, text="Currency Exchange Rate",anchor="w",font=("Times", 17, "bold",'underline'),pady=10).grid(sticky="W",row=0,column=0,columnspan=3)
variable = StringVar(m3)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(m3, variable, *OPTIONS)
w.configure(width=13)
w.grid(sticky="ew",row=2,column=0)
Label(m3, text="   ",anchor="w",font=("Times", 15, "bold")).grid(sticky="W",row=2,column=1)
Label(m3, text=" ",anchor="w",font=("Times", 15, "bold"),pady=10).grid(sticky="W",row=2,column=5)

def ok():
    id= variable.get()
    str=''
    label=''


    for i in list:
        if i==id:
            continue
        else:
            label=i
            str=str+i+','
    
    url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms='+id+'&tsyms='+str
    price= requests.get(url)
    response_json = price.json()
    #type(response_json) # The API returns a list
    x=5
    for i in range(1,8):
        
        if list[i]==id:
            continue
        if i==1:
            im=logoBTC
        elif i==2:
            im=logoETH
        elif i==3:
            im=logoXRP
        elif i==4:
            im=logoXLM
        elif i==5:
            im=logoLTC
        elif i==6:
            im=logoUSDT
        else:
            im=logoXMR
        
        Label(m3,text='1 '+id,anchor="w",font=("Times", 17, "bold")).grid(row=5,rowspan=5,column=0,columnspan=2)
        #Label(m3,image=im).grid(sticky="W",row=5,rowspan=5,column=1)
        Label(m3,image=im).grid(sticky="W",row=x,column=3)
        Label(m3, text=list[i],anchor="w",font=("Times", 15, "bold"),pady=10).grid(sticky="W",row=x,column=4)
        Label(m3, text=response_json[id][list[i]],anchor="w",font=("Times", 15, "bold")).grid(sticky="W",row=x,column=6)
        x=x+1

button = Button(m3, text="SELECT", command=ok)
button.config(width=12)
button.grid(sticky="W",row=2,column=2)







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
