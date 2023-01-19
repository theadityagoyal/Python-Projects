# x=1
# def show():
#     global x
#     x=x+1
#     if(x%2==0):
#         print("Ram")
#     else:
#         print('seeta')
# show()
# show()
# show()
# show()

from tkinter import *

root = Tk()
root.minsize(400, 400)

b1 = Button(root, text="click", font=("Arial", 20))

x = 1


def show(e):
    global x
    x = x + 1
    if (x % 2 == 0):
        root.configure(background="blue")
    else:
        root.configure(background="cyan")


# b1.bind("<Button>", show)
# b1.bind("<ButtonRelease>", show)
b1.bind("<Motion>", show)
b1.pack()
root.mainloop()
