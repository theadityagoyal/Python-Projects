i=1 
while i<=5:  
    n=int(input("Please enter numbers between 1 to 5 to see diffrent Exceptions : "))  
    if n==1:   
        try:    
            a=int(input("Please enter number a : "))    
            b=int(input("Please enter number b (put b=0): "))    
            c=a/b   
        except ZeroDivisionError:    
            print("Oops! Number Divisible by Zero Exception Occurs.")   
        else:    
            print("Division is",c)      
    elif n==2:   
        try:    
            a=int(input("Please enter number a : "))    
            b=int(input("Please enter number b (put b='a'): "))    
            c=a/b   
        except ValueError:    
            print("Oops! Value Error Exception Occurs.Please enter a valid number.")   	
        else:    
            print("Division is",c)	      
    elif n==3:   
        try:    
            a=int(input("Please enter number a : "))    
            b=int(input("Please enter number b : "))    
            c=k/b
        except NameError: 
            print("Oops! Name Error Exception Occurs due to c=k/b (k is not defined ).Please enter a valid variable number.")      
    elif n==4:   
        try:    
            r='2'+2   
        except TypeError:    
            print("Oops! Type Error Exception Occurs (due to '2'+2).Please Provide Valid data type. ")      
    elif n==5:   
        try:    
            n=int(input("Please enter Numbers between 2 to 3: (Check for other nos) "))
            assert n>=2 and n<=3    
            print("The Number Entered is",n)   
        except AssertionError:    
            print("Oops! Assertion Error Occurs..Please enter number between 2 to 3.")
        else:   
            print("Exiting The Program")   
            exit() 
    i+=1
