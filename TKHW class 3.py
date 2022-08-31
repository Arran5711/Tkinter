from tkinter import *

window=Tk()
def to_mph():
    mph=float(e2_value.get())
    in_hours=float(e2_value.get())
    distance=float(mph*in_hours)

    t1.delete("1.0",END)
    t1.insert(END,distance)

    t2.delete("1.0",END)
    t2.insert(END,in_hours)

    t3.delete("1.0",END)
    t3.insert(END,mph)

e2=StringVar()
e3=Label(window,text="mph")
e4=Label(window,text="time in hours")
e5=Label(window,text="distance")


t1=Text(window,height=1,width=20)
t2=Text(window,height=1,width=20)
t3=Text(window,height=1,width=20)

b1=Button(window,text="claculate",command=to_mph)

e2_value=StringVar()
e3.grid(row=0,column=0)
e4.grid(row=0,column=2)
e5.grid(row=1,column=1)
t1.grid(row=1,column=0)
t2.grid(row=1,column=2)
t3.grid(row=2,column=1)
b1.grid(row=0,column=1)

window.mainloop()