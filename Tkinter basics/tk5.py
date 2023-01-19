from tkinter import *
root=Tk()
root.geometry("400x400")
root.resizable(0,0)

def show():
    root.configure(background="green")

def show1():
     root.configure(background="blue")


def show2():
    root.configure(background="purple")


un=Button(root,text="Login",font=("Arial",13),fg="blue",bg="orange",command=show,border=5)
un.pack()
un1=Button(root,text="Login1",font=("Arial",13),fg="red",bg="orange",command=show1,border=5)
un1.pack()
un2=Button(root,text="Login2",font=("Arial",13),fg="green",bg="orange",command=show2,border=5)
un2.pack()
root.mainloop()