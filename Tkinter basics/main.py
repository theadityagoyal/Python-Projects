from tkinter import *
root=Tk()

# root.minsize(300,300) #minsize is used for jab 300 se size km nahi rakhna chate h 300 se chota nahi hoga
# root.maxsize(500,500)
root.geometry("900x500")
#When we want to fix the window size
root.resizable(0,0)
un=Label(root,text="Hi This\n is Aditya \nyoyo",font=("Algerian",15),bg="violet",fg="white",width="63",height="3")
un.pack()

root.mainloop()

'''
label,button,entry,checkbutton,Radiobutton,listbox,frame,menubutton,menu,canvas,scale,message,scrollbar,text,spinbox,toplevel,panedwindow,tkMessagebox,Labelbox

'''