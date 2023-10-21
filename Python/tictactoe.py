from tkinter import *
import random

def nexturn(r,c):
    global player

    if buttons[r][c]['text'] == '' and checkwinner() == False:

        if player == players[0]:

            buttons[r][c]['text'] = player

            if checkwinner() is False:
                player = players[1]
                label.config(text=players[1]+' turn')
            elif checkwinner() is True:
                label.config(text=players[0]+' winned')
            elif checkwinner() is 'Tie':
                label.config(text='Tie')

        else:

            buttons[r][c]['text'] = player

            if checkwinner() is False:
                player = players[0]
                label.config(text=players[0]+' turn')
            elif checkwinner() is True:
                label.config(text=players[1]+' winned')
            elif checkwinner() is 'Tie':
                label.config(text='Tie')



def checkwinner():
    
    for r in range(3):
        if buttons[r][0]['text'] == buttons[r][1]['text'] == buttons[r][2]['text'] != '':
            buttons[r][0].config(bg='red')
            buttons[r][1].config(bg='red')
            buttons[r][2].config(bg='red')
            return True
        
    for c in range(3):
        if buttons[0][c]['text'] == buttons[1][c]['text'] == buttons[2][c]['text'] != '':
            buttons[0][c].config(bg='red')
            buttons[1][c].config(bg='red')
            buttons[2][c].config(bg='red')
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='red')
        buttons[1][1].config(bg='red')
        buttons[2][2].config(bg='red')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='red')
        buttons[1][1].config(bg='red')
        buttons[2][0].config(bg='red')
        return True
    elif emptyspaces() is False:

        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg='yellow')
        return 'Tie'
    else:
        return False
    

def emptyspaces():
    Spaces = 9

    for r in range(3):
        for c in range(3):
            if buttons[r][c]['text'] != '':
                Spaces -=1
    
    if Spaces == 0:
        return False
    else:
        return True

def newgame():
    global player 

    player = random.choice(players)

    label.config(text=player+' turn')

    for r in range(3):
        for c in range(3):
            buttons[r][c]['text'] = ''
            buttons[r][c].config(bg='#F0F0F0')

window = Tk()
window.title('jogo da idosa')

players = ['O','X']
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(window,text= player + ' turn',font=('consolas',25))
label.pack(side=TOP)

resetbutton = Button(text='restart',font=('Comic sans MS',20),command=newgame)
resetbutton.pack()

frame = Frame(window)
frame.pack()

for r in range(3):
    for c in range(3):
        buttons[r][c] = Button(frame, text='', font=('Comic sans MS',25), width=6,height=2,command=lambda row=r,column=c : nexturn(row,column))
        buttons[r][c].grid(row=r,column=c)

window.mainloop()