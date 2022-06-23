from tkinter import *

root = Tk()
root.title("diet")

l1 = Label(text='enter age')
l2 = Label(text='enter weight')
l3 = Label(text='enter colorie intake per day')

l1.grid(row=0,column=0, sticky='w')
l2.grid(row=1,column=0, sticky='w')
l3.grid(row=2,column=0, sticky='w')

age=Entry().grid(row=0,column=1)
weight=Entry().grid(row=1,column=1)
Calories=Entry().grid(row=2,column=1)
root.mainloop()




