"""
#code for wieght coverter
from tkinter import *

window=Tk()
def from_kg():
    gram=float(e2_value.get())*1000
    pound=float(e2_value.get())*2.20462
    ounce=float(e2_value.get())*35.274

    t1.delete("1.0",END)
    t1.insert(END,gram)

    t2.delete("1.0",END)
    t2.insert(END,pound)

    t3.delete("1.0",END)
    t3.insert(END,ounce)

e1=Label(window,text="enter the wieght in kg")
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e3=Label(window,text="gram")
e4=Label(window,text="pound")
e5=Label(window,text="ounce")

t1=Text(window,height=1,width=20)
t2=Text(window,height=1,width=20)
t3=Text(window,height=1,width=20)

b1=Button(window,text="Convert",command=from_kg)

e1.grid(row=0,column=0)
e2.grid(row=0,column=1)
e3.grid(row=1,column=0)
e4.grid(row=1,column=1)
e5.grid(row=1,column=2)
t1.grid(row=2,column=0)
t2.grid(row=2,column=1)
t3.grid(row=2,column=2)
b1.grid(row=0,column=2)

window.mainloop()


"""
#code for temperature converter

from tkinter import *
import tkinter.font as font

def convert():
    temp_celsius=celsius_value.get()
    if(temp_celsius.replace('.','',1).isdigit()):
        error_msg.grid_forget()
        temp_farhenheit=(float(temp_celsius)*9/5)+32
        output_farhenheit.config(text="temperature in Farhenheit:"+str(temp_farhenheit))
    else:
        error_msg.grid(row=1,column=1)


window=Tk()
window.title("celsius to farhenhiet converter")


description=Label(text="celsius --> farhenhiet",font=font.Font(size=20),fg="grey")
description.pack()

frame=Frame()
frame.pack(pady=20)

message_one=Label(frame, text="enter tempreature in celsius:",font=font.Font(size=10))
message_one.grid(row=0,column=0)

celsius_value=Entry(frame)
celsius_value.grid(row=0,column=1)

error_msg=Label(frame,text="please enter a valid input",font=font.Font(size=8),fg="red")
output_farhenheit=Label(frame,font=font.Font(size=12))
output_farhenheit.grid(row=2,column=0,columnspan=2,pady=10)

submit_btn=Button(frame,text="convert",width=30,fg="black",bg="green", padx=20,command=convert)
submit_btn.grid(row=3, column=0, columnspan=2,pady=10)
window.geometry("500x260")
window.mainloop()


