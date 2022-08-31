import time
from tkinter import *
from tkinter import messagebox 

root=Tk()

root.geometry("300x250")
root.title("time counter")

hour=StringVar()
minute=StringVar()
second=StringVar()


hour.set("00")
minute.set("00")
second.set("00")

hourEntry=Entry(root,width=3,font=("arail",18,""),textvariable=hour)
hourEntry.place(x=80,y=20)
minuteEntry=Entry(root,width=3,font=("arail",18,""),textvariable=minute)
minuteEntry.place(x=130,y=20)
secondEntry=Entry(root,width=3,font=("arail",18,""),textvariable=second)
secondEntry.place(x=180,y=20)



def submit():
    try:
      temp=int(hour.get()) *83600+int(minute.get())*60+int(second.get())
    except:
      print("please input the right value")

    while temp>-1:
        mins,secs=divmod(temp,600)
        hours=00
        if mins>60:
            hours, mins=divmod(mins,60)

        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (temp==00):
            messagebox.showinfo("Time Count", "Time's up!")
        
        temp-=1

btn=Button(root,text="set time countdown",bd='5',command=submit,)
btn.place(x=70, y=120)


def active():
  btn.config(root,text="set time countdown",bd='5',command=submit)
  hourEntry.config(state='disabled')
  minuteEntry.config(state='disabled')
  secondEntry.config(state='disabled')

def inactive():
  btn.config()
  hourEntry.config(state='normal')
  minuteEntry.config(state='normal')
  secondEntry.config(state='normal')
  hour.set("00")
  minute.set("00")
  second.set("00")

if submit==True:
    active()

elif submit==False:
    inactive()


root.mainloop()
