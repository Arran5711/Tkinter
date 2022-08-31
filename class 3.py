from tkinter import*
import tkinter.font as font
import random


player_score=0
computer_score=0
options=[("rock",0),("paper",1),("scissors",2)]

def computer_wins():
    global player_score, computer_score
    computer_score+=1
    winner_label.config(text="computer won!!!")
    computer_score_label.config(text="computer score:"+str(computer_score))
    player_score_label.config(text="player score:"+str(player_score))

def player_wins():
    global player_score, computer_score
    player_score+=1
    winner_label.config(text="player won!!!")
    computer_score_label.config(text="computer score:"+str(computer_score))
    player_score_label.config(text="player score:"+str(player_score))

def tie():
    global player_score, computer_score
    winner_label.config(text="Tie!!!")
    computer_score_label.config(text="computer score:"+str(computer_score))
    player_score_label.config(text="player score:"+str(player_score))

def player_choice(player_input):
    global player_score,computer_score
    print(player_input)

    computer_input=get_random_choice()
    print(computer_input)

    player_choice_label.config(text="you selected:"+player_input[0])
    computer_choice_label.config(text="computer selected:"+computer_input[0])


    #if game tie
    if(player_input==computer_input):
        tie()

    #if player rock
    if(player_input[1]==0):
        if(computer_input[1]==1):
          computer_wins()
        elif(computer_input[1]==2):
            player_wins()

            #if player choose papper
    elif(player_input[1]==1):
        if(computer_input[1]==0):
            player_wins()
        elif(computer_input[1]==2):
            computer_wins()


            #if player scissors
    elif(player_input[1]==2):
        if(computer_input[1]==0):
            computer_wins()
        elif(computer_input[1]==1):
            player_wins()

def get_random_choice():
    return random.choice(options)

game_window=Tk()
game_window.title("rock paper scissors Game")

app_font=font.Font(size=12)

game_title=Label(text="rock paper scissors",fg="red",font=font.Font(size=20))
game_title.pack()

winner_label=Label(text="let the games begin",fg="blue",font=font.Font(size=13))
winner_label.pack()

input_frame=Frame(game_window)
input_frame.pack()

player_options=Label(input_frame,text="your options our:",font=app_font,fg="grey")
player_options.grid(row=0,column=0,padx=0,pady=8)

rock_btn=Button(input_frame,text="rock",width=15,bg="pink",pady=5,command=lambda: player_choice(options[0]))
rock_btn.grid(row=1,column=1,padx=8,pady=5)

papper_btn=Button(input_frame,text="papper",width=15,bg="silver",pady=5,command=lambda: player_choice(options[1]))
papper_btn.grid(row=1,column=2,padx=8,pady=5)

scissors_btn=Button(input_frame,text="scissors",width=15,bg="light blue",pady=5,command=lambda: player_choice(options[2]))
scissors_btn.grid(row=1,column=3,padx=8,pady=5)

score_label=Label(input_frame,text="score:",font=app_font,fg="grey")
score_label.grid(row=2,column=0)

player_choice_label=Label(input_frame,text="you selected:----",font=app_font)
player_choice_label.grid(row=3,column=1,padx=5)

player_score_label=Label(input_frame,text="your score:----",font=app_font)
player_score_label.grid(row=3,column=2,padx=5)

computer_choice_label=Label(input_frame,text="computer selected:----",font=app_font,fg="black")
computer_choice_label.grid(row=3,column=1,padx=5)

computer_score_label=Label(input_frame,text="computer score:----",font=app_font,fg="black")
computer_score_label.grid(row=4,column=2,padx=(10,0),pady=5)

game_window.geometry("700x300")
game_window.mainloop()