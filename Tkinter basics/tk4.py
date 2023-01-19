from tkinter import *
root=Tk()
root.minsize(500,500)
root.configure(background='darkblue')

un1=Label(root,text="Enter Name",font=("Arial",15))
un1.grid(row=0,column=0,pady=25,sticky='w')

e1=Entry(root,font=("Arial",15))
e1.grid(row=0,column=1)

un2=Label(root,text="Enter password",font=("Arial",15))
un2.grid(row=1,column=0,pady=18)

e2=Entry(root,show='*',font=("Arial",15))
e2.grid(row=1,column=1,sticky='w')

un=Button(root,text="Login",font=("Arial",20),fg="red")
un.grid(row=2,column=0,columnspan=3)


root.mainloop()