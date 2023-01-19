class Bank(object):
    cash=1000
     
    def available(cls):
        print(cls.cash)
class ABank(Bank):
    pass
class SBI(Bank):
    cash=2000
    
    def available(cls):
        print(cls.cash+Bank.cash)
a=ABank()
a.available()

s=SBI()
s.available()
