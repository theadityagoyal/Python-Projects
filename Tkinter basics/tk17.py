from tkinter import *
root= Tk()
root.background="blue"
root.geometry("500x500")
root.resizable(0, 0)



def show(b):
    b["bg"]="red"
    b["fg"]="pink"
    b["width"]=100
    b["height"]=5
    b["text"]="ADITYA GOYAL"


b1 = Button(root, text="yooooo", font=("Arial", 20), command=lambda :show(b1))
b1.pack()
root.mainloop()