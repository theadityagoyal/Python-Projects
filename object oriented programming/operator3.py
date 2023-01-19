class Bookx:
    def __init__(self, pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
class Booky:
    def __init__(self,pages):
        self.pages=pages


        

b1=Bookx(100)
b2=Booky(150)
print("total pages=",b1+b2)
