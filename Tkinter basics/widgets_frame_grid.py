from tkinter import *

class MyButtons:
    def __init__(self,root):
        self.f=Frame(root, height=500, width=600)

        self.f.propagate(0)

        self.f.pack()

        #create a push button and bind it to buttonClick method
        self.b1=Button(self.f, text='Click me', width=15, height=2, command=self.buttonClick)

        #create another button that closes the root window upon clicking
        self.b2=Button(self.f, text='close', width=15, height=2, command=quit)

        self.b1.grid(row=0, column=1)
        self.b2.grid(row=0,column=2)

        #self.b2.pack(side=RIGHT, padx=10, pady=15)

    #the event handler method
    def buttonClick(self):
        #create a label with some text
        self.lbl=Label(self.f, text="welcome to online session", width=40, height=5, font=('Courier', -30, 'bold underline'), fg='blue')

        #attach label in the frame
        self.lbl.grid(row=2, column=0)
root=Tk()

mb=MyButtons(root)

root.mainloop()

            
        
