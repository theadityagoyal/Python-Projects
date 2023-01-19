import math 
class Square:
    def area(self,x):
        print("Square area=",x*x)
class Circle:
    def area(self,x):
        print("Circle=",(math.pi*x*x))
c=Circle()
c.area(15)
b=Square()
b.area(5)
