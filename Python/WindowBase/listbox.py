from tkinter import *

window = Tk()

food_list = ['Pizza','Hamburger','hot dog','ice cream','water']

def submitP():
    food = []

    for i in listbox.curselection():
        food.insert(i,listbox.get(i))

    print(food)

def addP():
    if entrybox.get() == '':
         pass
    else:
        food_list.append(entrybox.get())
        listbox.insert(listbox.size(),entrybox.get())

        listbox.config(height=listbox.size())

def deleteP():

    for i in reversed(listbox.curselection()):

        listbox.delete(i)

    listbox.config(height=listbox.size())


listbox = Listbox(window,
                  bg='white',
                  fg='black',
                  font=('Constantia',15),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

count = 0
for i in food_list:
    listbox.insert(count,i)
    count += 1

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

button = Button(window,text='Submit',command=submitP)
button.pack()

addbutton = Button(window,text='Add',command=addP)
addbutton.pack()

deltebutton = Button(window,text='Delete',command=deleteP)
deltebutton.pack()

window.mainloop()