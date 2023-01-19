

class MyException(Exception):
    pass
def check(dict):
    for k,v in dict.items():
        print("name is {} and balance is {}" .format(k,v))
        if(v<2000):
            raise MyException("balance amount is less in account of "+k)
bank={'rahul':5000,'ajay':2000,'atul':1500}
try:
    check(bank)
except MyException as me:
    print(me)
