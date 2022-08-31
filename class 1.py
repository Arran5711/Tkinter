from tkinter import *
import calendar

def showcal():
    new_gui=Tk()
    new_gui.config(background="white")
    new_gui.title("calendar")
    new_gui.geometry("550x600")
    fetch_year=int(year_field.get())
    cal_content=calendar.calendar(fetch_year)
    cal_year=Label(new_gui,text=cal_content,font="consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    new_gui.mainloop()

if __name__=="__main__":
    gui=Tk()
    gui.config(background="white")
    gui.title("calendar")
    gui.geometry("250x140")
    cal=Label(gui,text="calender",bg="dark gray",font=("times",28,"bold"))
    year=Label(gui,text="Enter the year",bg="light green")
    year_field=Entry(gui)
    show=Button(gui,text="show calendar",fg="black",bg="red",command=showcal)
    Exit=Button(gui,text="exit",fg="black",bg="red",command=exit)
    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)
    year_field.grid(row=3,column=1)
    show.grid(row=4,column=1)       
    Exit.grid(row=5,column=1)

    gui.mainloop()


