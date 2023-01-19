class Student:  
    def __init__(self):
        print("Calling parent constructor") 
 
    def teacher(self):
       print("Overriding Teacher method in Parent Class") 
 
    def s_details(self):
       print(".........CALLING PARENT METHOD using Child Object......")
       self.roll=input("Enter Your Roll Number. -: ")
       self.name=input("Enter Your Name -: ")
       self.div=input("Enter Your Division -: ")
       self.city=input("Enter Your City -: ")
       print(" ")
       print("Student Details Are.....")
       print("Your Roll Number is",self.roll)
       print("Your Name is",self.name)
       print("Your Division is",self.div)
       print("Your City is",self.city) 
 
    def sum(self, a=None,b=None,c=None):
        print(" ")
        print(".........METHOD OVERLOADING WITH a=10,b=20 and c=30......")
        if a is not None and b is not None and c is not None :
           print('Sum of a,b and c is',a+b+c)
        elif a is not None and b is not None:
            print('Sum of a and b is',a+b)
        else:
            print('Sum Not possible..Value of a is',a) 
 
class College(Student): 
    def __init__(self):
        print("Calling child constructor")
         def teacher(self): 
             print(" ")
             print(".........METHOD OVERRIDING:Overriding Teacher method in Child Class")
             def c_details(self):
                 print(".........CALLING CHILD METHOD using Child Object......")
                 self.cname=input("Enter Your College Name -: ")
                 self.uni=input("Enter Your University Name -: ")
                 self.caddress=input("Enter Your College City  -: ")
                 print(" ")
                 print("Your College Details Are.....")
                 print("Your College name is",self.cname)
                 print("Your University is",self.uni)
                 print("Your College City is",self.caddress) 
 
 
c = College()        # instance of child
c.c_details()        # calls parent's method
c.s_details()        # calls parent's method
c.teacher()      # calls Overridden method
c.sum(10,20,30)      # Method overloading with three parameters
c.sum(10,20)         # Method overloading with two parameters
c.sum(10)            # Method overloading with one parameters 
