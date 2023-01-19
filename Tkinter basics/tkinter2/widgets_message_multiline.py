from tkinter import *
root=Tk()

class MyMessage():
    def __init__(self,root):

        self.f=Frame(root, height=350,width=500)

        self.f.propagate(0)

        self.f.pack()

        self.m=Message(self.f, text='This is a message that has more than one line of text', width=200, font=('Roman',20, 'bold italic'), fg='dark goldenrod')

        self.m.pack()
mb=MyMessage(root)
root.mainloop()
