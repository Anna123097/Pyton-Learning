from tkinter import *

root = Tk()

e = Entry(width=20)
b = Button(text='Преобразовать')
l = Label(bg = "black", fg='white', width='20')

def strToSortList(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

b.bind('<Button-1>', strToSortList)

e.pack()
b.pack()
l.pack()

root.mainloop()





from tkinter import *

root = Tk()

e = Entry(width=10)

b_plus = Button(text='+')
b_mult = Button(text='*')
b_minus = Button(text='-')
b_div = Button(text='/')


l = Label(bg = "black", fg='white', width='40')

def b_plus_(event):
    s = e.get()
    s = s.split()
    
    l['text'] = str(int(s[0]) + int(s[1]))

def b_minus_(event):
    s = e.get()
    s = s.split()
    
    l['text'] = str(int(s[0]) - int(s[1]))

def b_mult_(event):
    s = e.get()
    s = s.split()
    
    l['text'] = str(int(s[0]) * int(s[1]))

def b_div_(event):
    s = e.get()
    s = s.split()
    
    l['text'] = str(int(s[0]) / int(s[1]))


b_plus.bind('<Button-1>', b_plus_)
b_minus.bind('<Button-1>', b_minus_)
b_mult.bind('<Button-1>', b_mult_)
b_div.bind('<Button-1>', b_div_)


e.pack()


b_plus.pack()
b_mult.pack()
b_minus.pack()
b_div.pack()

l.pack()
root.mainloop()