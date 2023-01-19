from tkinter import *

root = Tk()
root.minsize(400, 400)
# root.bind("<Enter>",lambda e:root.configure(background="black"))
# root.bind("<Leave>",lambda e:root.configure(background="cyan"))

# root.bind("<a>",lambda e:root.configure(background="red"))
# root.bind("<b>",lambda e:root.configure(background="cyan"))
# root.bind("<c>",lambda e:root.configure(background="pink"))

# root.bind("<F1>",lambda e:root.configure(background="pink"))
# root.bind("<F2>",lambda e:root.configure(background="green"))
# root.bind("<F3>",lambda e:root.configure(background="orange"))
# root.bind("<Delete>",lambda e:root.configure(background="cyan"))

# root.bind("1",lambda e:root.configure(background="cyan"))#if we want to done operation with number than put values without angular brackets
# root.bind("2",lambda e:root.configure(background="red"))
# root.bind("3",lambda e:root.configure(background="blue"))

# root.bind("<Shift-Up>",lambda e:root.configure(background="cyan"))
# root.bind("<Shift-Down>",lambda e:root.configure(background="red"))
# root.bind("<Shift-Left>",lambda e:root.configure(background="blue"))
# root.bind("<Shift-Right>",lambda e:root.configure(background="green"))
# root.bind("<Alt-Up>",lambda e:root.configure(background="black"))
# root.bind("<Control-Up>",lambda e:root.configure(background="orange"))

b1 = Button(root, text="click", font=("Arial", 20))
b1.bind("<Button>", lambda e: root.configure(background="red"))
b1.bind("<ButtonRelease>", lambda e: root.configure(background="cyan"))
b1.pack()

root.mainloop()
