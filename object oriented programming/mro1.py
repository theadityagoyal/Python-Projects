class A(object):
    def method(self):
        print("a class method")
        #super().method()
class B(object):
    def method(self):
        print("b class method")
        #super().method()
class C(object):
    def method(self):
        print("c class method")
class X(A,B):
    def method(self):
        print("x class method")
        super().method()
class Y(B,C):
    def method(self):
        print("y class method")
        super().method()
class P(X,Y,C):
    def method(self):
        print("p class method")
        super().method()
p=P()
p.method()
