from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)


def show(e):
    root.configure(background="green")


def show1(e):
    root.configure(background="blue")


def show2(e):
    root.configure(background="purple")


b1 = Button(root, text="click", fg="blue", font=("Arial", 15), border=5)
b1.bind("<Button-1>", show)  # LEft mouse key
b1.bind("<Button-2>", show1)  # Wheel
b1.bind("<Button-3>", show2)  # Right
b1.pack()
root.mainloop()
