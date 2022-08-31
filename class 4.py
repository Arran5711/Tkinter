from tkinter import*
from tkinter.ttk import*
import random
import time

from time import strftime

root=Tk()
root.title('clock')




for i in range(86400):
  time.sleep(1)
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  root.config(bg="r,g,b")


def time():
    string=strftime('%H:%M:%S:%p')
    lbl.config(text=string)
    lbl.after(100,time)


lbl=Label(root,font=('calibri',40,'bold'),
          background='orange',
          foreground='white')

lbl.pack(anchor='center')
time()
mainloop()