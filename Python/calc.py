from tkinter import *

def buttonpress(Num):
    global equation_Text

    equation_Text = equation_Text + str(Num)
    equationlabel.set(equation_Text)

def equals():
    
    global equation_Text 
    try:
        total = str(eval(equation_Text))

        equationlabel.set(total)

        equation_Text = total
    except ZeroDivisionError:
        print(' why are you trying to divide by 0')

        equation_Text = ""
    except SyntaxError:
        print(' syntax error')

        equation_Text = ""

def clear():
    global equation_Text

    equation_Text = ""

    equationlabel.set('')

window = Tk()
window.title('calculator')
window.geometry('500x500')

equation_Text = ""

equationlabel = StringVar()

label = Label(window,textvariable=equationlabel,font=('consolas',20),width=25,height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35,command=lambda : buttonpress(1))
button1.grid(row=0,column=0)
button2 = Button(frame,text=2,height=4,width=9,font=35,command=lambda : buttonpress(2))
button2.grid(row=0,column=1)
button3 = Button(frame,text=3,height=4,width=9,font=35,command=lambda : buttonpress(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=4,width=9,font=35,command=lambda : buttonpress(4))
button4.grid(row=1,column=0)
button5 = Button(frame,text=5,height=4,width=9,font=35,command=lambda : buttonpress(5))
button5.grid(row=1,column=1)
button6 = Button(frame,text=6,height=4,width=9,font=35,command=lambda : buttonpress(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=4,width=9,font=35,command=lambda : buttonpress(7))
button7.grid(row=2,column=0)
button8 = Button(frame,text=8,height=4,width=9,font=35,command=lambda : buttonpress(8))
button8.grid(row=2,column=1)
button9 = Button(frame,text=9,height=4,width=9,font=35,command=lambda : buttonpress(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,height=4,width=9,font=35,command=lambda : buttonpress(0))
button0.grid(row=3,column=1)

Plus = Button(frame,text='+',height=4,width=9,font=35,command=lambda : buttonpress('+'))
Plus.grid(row=3,column=0)
Minus = Button(frame,text='-',height=4,width=9,font=35,command=lambda : buttonpress('-'))
Minus.grid(row=3,column=2)
Times = Button(frame,text='*',height=4,width=9,font=35,command=lambda : buttonpress('*'))
Times.grid(row=0,column=3)
Divide = Button(frame,text='/',height=4,width=9,font=35,command=lambda : buttonpress('/'))
Divide.grid(row=1,column=3)
Decimal = Button(frame,text='.',height=4,width=9,font=35,command=lambda : buttonpress('.'))
Decimal.grid(row=0,column=4)
Equal = Button(frame,text='=',height=4,width=9,font=35,command=equals)
Equal.grid(row=2,column=3)
Delete = Button(frame,text='Del',height=4,width=9,font=35,command=clear)
Delete.grid(row=3,column=3)

# i hate how this code looks but uuhh idk what i should do 

window.mainloop()