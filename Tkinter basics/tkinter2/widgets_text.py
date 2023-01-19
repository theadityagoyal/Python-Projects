from tkinter import *
root=Tk()

class MyText:
    def __init__(self, root):
        self.t=Text(root,width=50, height=40,font=('Verdana',14,'bold'),fg='blue',bg='yellow',wrap=NONE)
        self.t.insert(END, 'this text\nwidget is of \n multiple line \n and so on and on\n')

        self.t.pack(side=LEFT)

        #show image in text widget
        self.img=PhotoImage(file='moon.gif')
        self.t.image_create(END, image=self.img)

        #create a tag with name 'start'
        self.t.tag_add('start','1.0','1.11')

        #apply colors to the tag
        self.t.tag_config('start', background='red',foreground='white',font=('Lucida consle', 20,'bold italic'))

        #create a scrollbar widget to move the text vertically
        #self.s=Scrollbar(root,orient=VERTICAL,command=self.t.yview)

        self.h=Scrollbar(root,orient=HORIZONTAL,command=self.t.xview)

        #attach the scrollbar to the Text widget
        #self.t.configure(yscrollcommand=self.s.set)
        self.t.configure(xscrollcommand=self.h.set)

        #self.s.pack(side=RIGHT, fill=Y)
        self.h.pack(side=BOTTOM, fill=X)

        

mt=MyText(root)
root.mainloop()
