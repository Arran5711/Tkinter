from tkinter import *


window=Tk()


b1=Button(window,text="bg blue",bg="blue",activebackground="blue")
b2=Button(window,text="bg red",bg="red",activebackground="red")
b3=Button(window,text="bg green",bg="green",activebackground="green")


t1=Text(window,height=5,width=20)
t2=Text(window,height=5,width=20)
t3=Text(window,height=5,width=20)

b1.grid(row=1,column=2,)
b2.grid(row=2,column=2)
b3.grid(row=3,column=2)

window.mainloop()
