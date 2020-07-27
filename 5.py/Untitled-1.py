"""
from tkinter import *
root = Tk()
c = Canvas(width=300, height=300, bg='white')
c.focus_set()
c.pack()
 
ball = c.create_oval(140, 140, 160, 160, fill='green')
c.bind('<Up>', lambda event: c.move(ball, 0, -2))
c.bind('<Down>', lambda event: c.move(ball, 0, 2))
c.bind('<Left>', lambda event: c.move(ball, -2, 0))
c.bind('<Right>', lambda event: c.move(ball, 2, 0))
 
root.mainloop()
"""
from tkinter import *
 
root = Tk()
c = Canvas(root, width=500, height=500, bg="white")
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')
ball2=c.create_oval(0, 100, 40, 145, fill='green')
prengel = c.create_polygon(100, 100, 300, 150, 200, 200, fill='green')
 
def motion():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)


def motionUDown():
    c.move(ball, 0, 1)
    if c.coords(ball)[2] < 300:
        root.after(10, motionUDown)

def motion_pren():
    c.move(prengel, 1, 0)
    if c.coords(prengel)[2] < 500:
        root.after(10, motion_pren) 

def motionu():
    c.move(ball2, 0, 1)
    if c.coords(ball2)[3] < 300:
        root.after(10, motionu)

motion()
motionUDown()
motion_pren()
motionu()
root.mainloop()