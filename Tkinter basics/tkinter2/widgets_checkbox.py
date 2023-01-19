from tkinter import *

class Mycheck:
    def __init__(self,root):
        self.f=Frame(root,height=350,width=500)

        self.f.propagate(0)

        self.f.pack()

        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()

        self.c1=Checkbutton(self.f, bg='yellow',fg='green', font=('Georgia', 20, 'underline'), text='Java', variable=self.var1, command=self.display)
        self.c2=Checkbutton(self.f, bg='yellow',fg='green', font=('Georgia', 20, 'underline'), text='Python', variable=self.var2, command=self.display)
        self.c3=Checkbutton(self.f, bg='yellow',fg='green', font=('Georgia', 20, 'underline'), text='.NET', variable=self.var3, command=self.display)

        self.c1.place(x=50,y=100)
        self.c2.place(x=200,y=100)
        self.c3.place(x=350,y=100)
    def display(self):
        x=self.var1.get()
        y=self.var2.get()
        z=self.var3.get()

        str=''

        if x==1:
            str+='Java\t'
        if y==1:
            str+='Python\t'
        if z==1:
            str+='.Net'
        lb=Label(text=str,fg='blue').place(x=50,y=150,width=200,height=20)
root=Tk()
mb=Mycheck(root)
root.mainloop()
