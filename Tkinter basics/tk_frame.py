from tkinter import *

#method to be called when the button(widget) is clicked
def buttonClick(self):
    print('You have clicked me')

#create root window
root=Tk()

#give title for root window
root.title("My Frame")

#create a frame as child to root window
f=Frame(root, height=400,width=500,bg="yellow", cursor="cross")

#attach the frame to root window
f.pack()

#create a push button as child to frame (widget)
b=Button(f, text='My Button', width=15, height=2, bg='yellow', fg='blue', activebackground='green', activeforeground='red')

#attach button to frame
b.pack()

#bind left mouse button with the method to be called
b.bind("<Button-1>",buttonClick)

#let the root window wait for any events
root.mainloop()
