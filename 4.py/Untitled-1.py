from tkinter import *

root = Tk()
root.geometry("400x400")

c = Canvas(root, width=200, height=200, bg='red')
c.pack()

c.create_line(150, 100, 150, 150)
c.create_line(100, 100, 100, 150)

c.create_line(100, 150, 150, 150)
c.create_line(100, 100, 150, 100)

c.create_line(100, 100, 125, 50)
c.create_line(150, 100, 125, 50)

c.create_rectangle(100, 100, 115, 115)

c.create_rectangle(130,125,150,150)

c.create_oval(125,125,130,130)

c.create_rectangle(20,20,180,180)
c.create_oval(20,20,180,180)



root.mainloop()