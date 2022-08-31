from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title('bg color changer')

title = Label(window, text="change bg color")
caption = Label(window, text="choices")

title.grid(row=0, column=0, columnspan=3, pady=25)
caption.grid(column=0, row=1, padx=10)

#combobox
theNum = IntVar()
color = Combobox(window, textvariable=theNum, width=5)
color.insert(0, 'red')
color.insert(1, 'green')
color.insert(2, 'blue')

#radiobuttons
endVal = IntVar()
add= Radiobutton(window, text="add", variable=endVal, value="add")
delete = Radiobutton(window, text="delete", variable=endVal, value="delete")


#set a default value for endVal
endVal.set(10)

color.grid(column=1, row=1)
add.grid(column=2, row=1)
delete.grid(column=2, row=2, padx=30)


def colors():
  tables=""
  for i in range(endVal.get()+1):
    tables+=str(theNum.get())+"X"+str(i)+"="+str(theNum.get()*i)+"\n"
  table.configure(text=tables)

generateButton=Button(window, text="change color",command=colors)
table=Label(window,anchor="center")

generateButton.grid(row=4,column=1)
table.grid(row=5,column=1,pady=25)

window.mainloop()