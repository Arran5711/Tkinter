from tkinter import *

window=Tk()
def from_kg():
    CNY=float(e2_value.get())*8.10
    USD=float(e2_value.get())*1.20
    EUR=float(e2_value.get())*1.18

    t1.delete("1.0",END)
    t1.insert(END,CNY)

    t2.delete("1.0",END)
    t2.insert(END,USD)

    t3.delete("1.0",END)
    t3.insert(END,EUR)

e1=Label(window,text="enter the currency in GBP")
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e3=Label(window,text="CNY")
e4=Label(window,text="USD")
e5=Label(window,text="EUR")


t1=Text(window,height=1,width=20)
t2=Text(window,height=1,width=20)
t3=Text(window,height=1,width=20)

b1=Button(window,text="Convert",command=from_kg)

e1.grid(row=0,column=0)#text
e2.grid(row=0,column=1)
e3.grid(row=1,column=0)
e4.grid(row=1,column=1)
e5.grid(row=1,column=2)
t1.grid(row=2,column=0)
t2.grid(row=2,column=1)
t3.grid(row=2,column=2)
b1.grid(row=0,column=2)

window.mainloop()