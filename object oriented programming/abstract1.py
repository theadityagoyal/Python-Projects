#abstract class example
from abc import ABC, abstractmethod  #abc is abstract base class module
                                     #and ABC is metaclass
class Myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass
class Sub1(Myclass):
    def calculate(self,x):
        print('Square value=',x*x)

import math
class Sub2(Myclass):
    def calculate(self,x):
        print('Square root=',math.sqrt(x))

class Sub3(Myclass):
    def calculate(self,x):
        print('Cube value=',x**3)



obj1=Sub1()
obj1.calculate(16)

obj2=Sub2()
obj2.calculate(16)

obj3=Sub3()
obj3.calculate(16)
    
