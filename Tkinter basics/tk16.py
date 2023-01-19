from tkinter import *
root= Tk()
root.background="blue"
root.geometry("500x500")
root.resizable(0, 0)



def show(b):
    b["bg"]="cyan"
    b["fg"]="pink"
    b["width"]=10
    b["height"]=15
    b["text"]="ADITYA GOYAL"


b1 = Button(root, text="", font=("Arial", 20), command=show(1))
b1.pack()
root.mainloop()