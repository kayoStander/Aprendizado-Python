from tkinter import *

window = Tk()

foods = ['pizza','hamburger','hot dog']

Images = [PhotoImage(file='WindowImage.png'),PhotoImage(file='WindowImage.png'),PhotoImage(file='WindowImage.png')]

x = IntVar()

def order():
    if (x.get()==0):
        print('you choosed pizza')
    elif (X.get()==1):
        print('you choosed hamburger')
    elif (x.get()==2):
        print('you picked hot dog')

for i in range(len(foods)):
    radiobutton = Radiobutton(window, 
                              text=foods[i],
                              variable=x,
                              value=i,
                              font=('Comic Sans', 30),
                              indicatoron=0,
                              width=25,
                              command=order)#image=Images[i])
    radiobutton.pack(anchor='w')

window.mainloop()