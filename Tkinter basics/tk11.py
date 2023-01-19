from tkinter import *


root= Tk()
root.geometry("500x500")
root.resizable(0, 0)

# e1=Entry(root,font=("Arial",20))
# e1.bind("<FocusIn>",lambda e:root.configure(background="black"))
# e1.bind("<FocusOut>",lambda e:root.configure(background="blue"))
# e1.pack()
#
# e2=Entry(root,font=("Arial",20))
# e2.pack()

x=StringVar()
e1 = Entry(root, font=("Arial", 20),textvariable=x)
e1.pack()


def show():
    s = x.get()
    print(s)
    x.set("")#THis function clear the entry 

b1 = Button(root, text="click", font=("Arial", 20), command=show)
b1.pack()
root.mainloop()
