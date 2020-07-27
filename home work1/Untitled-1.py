from tkinter import *
 
root = Tk()
c = Canvas(root, width=500, height=500, bg="white")
c.pack()

ball = c.create_oval(150, 150, 200, 200, fill='green')
ball2=c.create_oval(0, 100, 40, 140, fill='red')
ball3 = c.create_oval(0, 100, 40, 140, fill='red')
ball4 = c.create_oval(0, 100, 40, 140, fill='green')
def motion():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)


def motionUDown():
    c.move(ball, 0, 1)
    if c.coords(ball)[2] < 300:
        root.after(10, motionUDown)

def motion_oval():
    c.move(ball3, 1, 0)
    if c.coords(ball3)[2] < 500:
        root.after(10, motion_oval) 

def motionu():
    c.move(ball2, 0, 1)
    if c.coords(ball2)[3] < 300:
        root.after(10, motionu)

def motionu_o():
    c.move(ball4, 1, 0)
    if c.coords(ball4)[3] < 300:
        root.after(10, motionu_o)

motion()
motionUDown()
motion_oval()
motionu()
motionu_o()
root.mainloop()