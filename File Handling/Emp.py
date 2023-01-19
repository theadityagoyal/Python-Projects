class Emp:
    def  __init__(self, id,  name, salary):
        self.id=id
        self.name=name
        self.salary=salary
	
    def display(self):
        print('id=',self.id)
        print('name=',self.name)
        print('salary=',self.salary)
class Myclass:

    
#method to receive Emp class instance and display
    @staticmethod
    def mymethod(e):
        e.salary+=1000;
        e.display()
e=Emp(10,'Raj Kumar',15000.75)
Myclass.mymethod(e)
