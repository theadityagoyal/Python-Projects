

num1 = int(input('Enter first number: '))
operation=int(input('Enter the operation:\nPress number: \n1.Addition\n2.Substraction\n3.Multiply\n4.Division\n5.Power\n6.Sqare-root\n'))
num2 = int(input('Enter Second number: '))

if operation==1:
    num3=num1+num2
    print('Addition of',num1,'+',num2,'=',num3)
elif operation==2:
    num3=num1-num2
    print('Substraction of',num1,'-',num2,'=',num3)
elif operation==3:
    num3=num1*num2
    print('Multiply of',num1,'*',num2,'=',num3)
elif operation==4:
    num3=num1/num2
    print('Division of',num1,'/',num2,'=',num3)
elif operation==5:
    num3=num1**num2
    print('power of',num1,'power',num2,'=',num3)
elif operation==6:

    print('square-root of',num1,'is',num1**(1/2))
else:
    print('Invalid input!')