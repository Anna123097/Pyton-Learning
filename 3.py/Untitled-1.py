from tkinter import *

root = Tk()
root.geometry("400x400")

c = Canvas(root, width=200, height=200, bg='green')
c.pack()

c.create_line(150, 100, 150, 150)
c.create_line(100, 100, 100, 150)

c.create_line(100, 150, 150, 150)
c.create_line(100, 100, 150, 100)

c.create_line(100, 100, 125, 50)
c.create_line(150, 100, 125, 50)

c.create_line(130,120,100,120)
c.create_line(120,100,130,125)

c.create_line(130,140,150,150)
root.mainloop()