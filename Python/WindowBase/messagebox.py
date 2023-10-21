from tkinter import *
from tkinter import messagebox

window = Tk()

def clickP():
    #messagebox.showinfo(title=' this is a infomessage',message=' this is the message')
    #messagebox.showwarning(title=' this is a warning',message=' this is the virus message if you know you know')
    #messagebox.showerror(title=' this is a error',message=' this is the error')

    #if messagebox.askokcancel(title=' ask ok cancel',message=' do you wanna do the thingy?'):
     #   print('yea')
    #else:
     #   print('no')

    #if messagebox.askretrycancel(title=' ask ok cancel',message=' do you wanna to retry the thingy?'):
     #   print('retryied')
    #else:
     #   print('not retryied')

    #if messagebox.askyesno(title=' ask yes or no',message=' yes or no?'):
     #   print('yeas')
    #else:
     #   print('noah')

    #ans = messagebox.askquestion(title=' ask question',message=' do ya like pie?')
    #if ans == 'yes':
     #   print(' wowa')
    #else:
     #   print(' nooo')

    ans = messagebox.askyesnocancel(title='yes no cancel', message='do you like to do you like to',icon='error')
    if ans == True:
        print('true')
    elif ans == False:
        print('false')
    else:
        print('none')

button = Button(window,
                command=clickP,
                text='click me')

button.pack()

window.mainloop()