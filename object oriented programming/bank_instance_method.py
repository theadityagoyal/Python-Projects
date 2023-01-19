import sys
class Bank(object):
    #initialize name and balance instance vars
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

 #to deduct withdrawal amount from balance
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=(self.balance)-amount
            return self.balance
        else:
            print("Insuffucient Funds")
            

    #to add deposit amount to balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance

   

#using Bank class create an account with name and balance 0.00
name=input("enter name: ")
b=Bank(name) # passing name variable value to constructor via instance

    #repeat continously till choice is 'e' or 'E'
while(True):
    print('d -Deposit, w- withdraw, e-Exit')
    choice=input("Your choice: ")
    if choice=='e' or choice=='E':
        sys.exit()
    #amount  for deposit or withdraw
    amount=int(input('Enter amount: '))

    #do transaction
    if choice=='d' or 'D':
        print('Balance after deposit:', b.deposit(amount))
    elif choice=='w' or 'W':
        print('balance after withdrawal: ', b.withdraw(amount))
    
    

    
