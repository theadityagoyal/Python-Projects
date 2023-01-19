from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)

show = lambda e: root.configure(background="green")
show1 = lambda e: root.configure(background="red")
show2 = lambda e: root.configure(background="blue")

b1 = Button(root, text="click", fg="blue", font=("Arial", 15), border=5)
# b1.bind("<Button-1>",show)#LEft mouse key
# b1.bind("<Button-2>",show1)#Wheel
# b1.bind("<Button-3>",show2)#Right

# IF we want the click button work with thew double then use double
# b1.bind("<Double-1>",show)#LEft mouse key
# b1.bind("<Double-2>",show1)#Wheel
# b1.bind("<Double-3>",show2)#Right

b1.bind("<Enter>", show)  # LEft mouse key
b1.bind("<Leave>", show1)  # Wheel
b1.bind("<Double-3>", show2)  # Right
b1.pack()
root.mainloop()
