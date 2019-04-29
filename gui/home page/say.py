
import requests




from tkinter import *

OPTIONS = [
"BTC",
"ETH",
"XRP",
"BCH",
"LTC",
"ADA",
"XMR"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
    id= variable.get()



    str=''

    list=['USD','BTC','ETH','XRP','BCH','LTC','ADA','XMR']
    for i in list:
        if i==id:
            continue
        else:
            str=str+i+','
    
    url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms='+id+'&tsyms='+str
    price= requests.get(url)
    response_json = price.json()
    #type(response_json) # The API returns a list
    for i in list:
        if i==id:
            continue
        else:
            print(i,response_json[id][i])
        
# Bitcoin data is the first element of the list


button = Button(master, text="OK", command=ok)
button.pack()

mainloop()
