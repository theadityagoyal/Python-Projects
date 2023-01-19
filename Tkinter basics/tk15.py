from tkinter import *
root= Tk()
root.background="blue"
root.geometry("500x500")
root.resizable(0, 0)

x=IntVar()
e1 = Entry(root, font=("Arial", 20),textvariable=x)
e1.pack()

def show():
    a=x.get()
    for i in range(1,11):
        print(a,'*',i,'=',a*i)
    x.set("")
    print("*************************End***********************\n")


b1 = Button(root, text="Table", font=("Arial", 20), command=show)
b1.pack()
root.mainloop()