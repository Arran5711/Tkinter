import tkinter
import math
import tkinter.messagebox
import random

root=tkinter.Tk()
root.minsize(350,260)
root.title('guess the number game')

number=random.randint(1,20)

def check_number():
    guess=text_guess.get()
    guess=int(guess)
    if guess>number:
        tkinter.messagebox.showinfo("high","Your guess is to high!")
    if guess<number:
            tkinter.messagebox.showinfo("low","Your guess is to low")
    if guess==number:
            tkinter.messagebox.showinfo("good!","Your guess is right! good job!")


def btn_confirm():
    myname=text_name.get()
    tkinter.messagebox.showinfo("Name","well "+myname+" i am thinking of a number between 1-20")


label=tkinter.Label(root,text="welcome to our game")
label.pack()

label_name=tkinter.Label(root,text="what is your name?")
label_name.place(x=10,y=60)
text_name=tkinter.Entry(root, width=20)
text_name.place(x=10,y=90)

btnok=tkinter.Button(root, text="ok",command=btn_confirm)
btnok.place(x=200,y=90,height=28)

label_guess=tkinter.Label(root,text='take a guess')
label_guess.place(x=10,y=150)
text_guess=tkinter.Entry(root,width=10)
text_guess.place(x=90,y=150)
btncheck=tkinter.Button(root, text='guess',command=check_number)
btncheck.place(x=200,y=150,width=45,height=28)

root.mainloop()