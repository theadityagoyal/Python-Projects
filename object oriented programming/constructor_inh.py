class Father:
    def __init__(self):
        self.property=800000.00
    def display_property(self):
        print('Father\'s property=',self.property)
class Son(Father):
    pass # we don't want to write anything in subclass
s=Son()
s.display_property()
