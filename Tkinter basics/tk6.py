from tkinter import *
root=Tk()
root.geometry("400x400")
root.resizable(0,0)

def show(e):
    root.configure(background="pink")


un=Button(root,text="Login",font=("Arial",13),fg="blue",bg="orange",border=5)
# un.config(command=show2)
un.bind("<Button>",show)
un.pack()

root.mainloop()