import os
from tkinter import *
from tkinter import filedialog,colorchooser,font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title='Font color:')
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(),size_box.get()))

def new_file():
    window.title('Untitled')
    text_area.delete('1.0',END)

def open_file():
    filer = askopenfilename(defaultextension='.txt', filetypes=[('All files', '*.*'), ('Text documents', '*.txt')])

    try:
        window.title(os.path.basename(filer))
        text_area.delete('1.0',END)

        filer = open(filer,'r')

        text_area.insert('1.0',filer.read())

    except Exception as e:

        print('Error is: ', e)

    finally:
        print('File Closed')

def save_file():
    filer = filedialog.asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All files', '*.*'),('Text documents', '*.txt')])

    if filer is None:
        return
    
    else:
        try:
            window.title(os.path.basename(filer))
            filer = open(filer,'w')

            filer.write(text_area.get('1.0',END))

        except Exception as e:

            print('Error is: ', e)

        finally:
            print('File Closed')

def cut():
    text_area.event_generate('<<Cut>>')

def copy():
    text_area.event_generate('<<Copy>>')

def paste():
    text_area.event_generate('<<Paste>>')

def about():
    showinfo('About us','Read files program')

def quiter():
    window.destroy()


window = Tk()
window.title('notepad')
Now_File = None

window_width,window_height = 500,500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry('{}x{}+{}+{}'.format(window_width,window_height,x,y))

font_name = StringVar(window)
font_name.set('Comic sans')

font_Size = StringVar(window)
font_Size.set('25')

text_area = Text(window,font=(font_name.get(),font_Size.get()))

scrollbar = Scrollbar(text_area)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scrollbar.set)

window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

colorbutton = Button(frame, text='Color',command=change_color)
colorbutton.grid(row=0,column=0)

fontbox = OptionMenu(frame, font_name, *font.families(),command=change_font)
fontbox.grid(row=0,column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_Size,command=change_font)
size_box.grid(row=0,column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=file_menu)

file_menu.add_command(label='New file',command=new_file)
file_menu.add_command(label='Open file',command=open_file)
file_menu.add_command(label='Save file',command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=quiter)

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Edit',menu=edit_menu)

edit_menu.add_command(label='Cut',command=cut)
edit_menu.add_command(label='Copy',command=copy)
edit_menu.add_command(label='Paste',command=paste)

help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Help',menu=help_menu)

help_menu.add_command(label='About',command=about)

window.mainloop()