from tkinter import *
root= Tk()
root.geometry("500x500")
root.resizable(0, 0)

x=IntVar()#for decimal use Double
y=IntVar()
z=IntVar()

e1 = Entry(root, font=("Arial", 20),textvariable=x)
e1.pack()

e2 = Entry(root, font=("Arial", 20),textvariable=y)
e2.pack()
def show():
    a = x.get()
    b=y.get()
    c=a+b
    z.set(c)


b1 = Button(root, text="click", font=("Arial", 20), command=show)
b1.pack()
e3 = Entry(root, font=("Arial", 20),textvariable=z)
e3.pack()


root.mainloop()
