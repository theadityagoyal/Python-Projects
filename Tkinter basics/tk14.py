from tkinter import *
root= Tk()
root.background="blue"
root.geometry("500x500")
root.resizable(0, 0)

x=DoubleVar()#for decimal use Double
y=DoubleVar()
z=DoubleVar()

e1 = Entry(root, font=("Arial", 20),textvariable=x)
e1.pack()

e2 = Entry(root, font=("Arial", 20),textvariable=y)
e2.pack()
def show(op):
    a = x.get()
    b=y.get()
    if (op==1):
        c=a+b
        z.set(c)
    if op==2:
        c=a-b
        z.set(c)
    if op==3:
        c=a*b
        z.set(c)
    if op==4:
        c=a+b
        z.set(c)
    if op==5:
        c=a**b
        z.set(c)


b1 = Button(root, text="+", font=("Arial", 20), command=lambda :show(1))
b1.pack()
b2 = Button(root, text="-", font=("Arial", 20), command=lambda :show(2))
b2.pack()
b3 = Button(root, text="*", font=("Arial", 20), command=lambda :show(3))
b3.pack()
b4 = Button(root, text="/", font=("Arial", 20), command=lambda :show(4))
b4.pack()
b5 = Button(root, text="power", font=("Arial", 20), command=lambda :show(5))
b5.pack()

e3 = Entry(root, font=("Arial", 35),textvariable=z)
e3.pack()


root.mainloop()
