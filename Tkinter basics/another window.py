from tkinter import *
import sqlite3
t=Tk()
t.geometry("400x400")
t.configure(background="pink")
a=StringVar()
b=StringVar()

def show():
    db=sqlite3.connect("Aditya goyal")
    cr=db.cursor()
    cr.execute("insert into login values('"+a.get()+"','"+b.get()+"')")
    db.commit()
    db.close()

    print("Data Insert")
    a.set("")
    b.set("")
def login():
    f2 = Frame(bg="#091e42")
    f2.place(x=0, y=0, width=425, height=350)

    u = Label(f2, text="LogIn Page", fg="white", font=("Century", 15), bg="#091e42")
    u.place(x=150, y=20)

    u1 = Label(f2, text="Enter Username", font=("Century", 15), bg="#091e42", fg="white")
    u1.place(x=50, y=80)
    e1 = Entry(f2, font=("", 15), width=15)
    e1.place(x=210, y=85)

    u2 = Label(f2, text="Enter password", font=("Century", 15), bg="#091e42", fg="white")
    u2.place(x=50, y=120)
    e2 = Entry(f2, show="*", width=15, font=("", 15))
    e2.place(x=210, y=125)

    b2 = Button(f2, text="<", font=("Century", 10), fg='red', command=home, bg="black")
    b2.place(x=1, y=0)

    b3 = Button(f2, text="LogIn", font=("Century", 15), fg='white', command=show, bg="red")
    b3.place(x=175, y=175, width=80, height=40)

#
# def regis():
#     f3 = Frame(bg="#091e42")
#     f3.place(x=0, y=0, width=425, height=350)
#
#     u = Label(f3, text="ReGisTerD", font=("Century", 15), bg="#091e42", fg="white")
#     u.place(x=150, y=20)
#
#     u1 = Label(f3, text="Enter Username", font=("Century", 15), bg="#091e42", fg="white")
#     u1.place(x=50, y=80)
#     e1 = Entry(f3, font=("", 15), width=15)
#     e1.place(x=225, y=85)
#
#     u2 = Label(f3, text="Enter password", font=("Century", 15), bg="#091e42", fg="white")
#     u2.place(x=50, y=120)
#     e2 = Entry(f3, show="*", width=15, font=("", 15))
#     e2.place(x=225, y=125)
#
#     u3 = Label(f3, text="Confirm password", font=("Century", 15), bg="#091e42", fg="white")
#     u3.place(x=50, y=160)
#     e3 = Entry(f3, show="*", width=15, font=("", 15))
#     e3.place(x=225, y=160)
#
#     b2 = Button(f3, text="<", font=("Century", 10), fg='white', command=login, bg="black")
#     b2.place(x=1, y=0)
#
#     b3 = Button(f3, text="Regis", font=("Century", 15), fg='white', command=login, bg="red")
#     b3.place(x=175, y=210, width=80, height=40)


def home():
    f1 = Frame(bg="#091e42")
    f1.place(x=0, y=0, width=425, height=350)
    u1 = Label(f1, text="**********_InstaGram_***********", font=("Century", 15), bg="#091e42", fg="white")
    u1.place(x=50, y=250)

    b1 = Button(f1, text="Instagram", font=("Century", 15), fg='white', bg="#091e42")
    b1.place(x=160, y=60, width=100, height=40)

    b2 = Button(f1, text="login", font=("Century", 15), fg='white', command=login, bg="#091e42")
    b2.place(x=120, y=120, width=80, height=40)

    b3 = Button(f1, text="Create New\nAccount", font=("Century", 12), fg='white', command=login, bg="#091e42")
    b3.place(x=210, y=120, width=100, height=40)


home()

t.mainloop()
