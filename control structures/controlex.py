#Control Structures remember the indentations
print("--Finding MAX BETWEEN 3 Nos using IF-Else-Elif STATEMENT--")
a=input("Enter value of First element:")
b=input("Enter value of Second element:")
c=input("Enter value of Third element:")
if a>b and a>c:
    print(a,"is Greater")
elif b>c:
    print(b,"is Greater")
else:
    print(c,"is Greater")
print("")



print("-----Calculate Factorial using WHILE LOOP-----------")
num=int(input("Enter the number : "))

fact=1
i=1
while i <= num:
    fact=fact*i
    i=i+1
    print("Factorial of",num," is :",fact)


    
print("-----Generate Fibonacci series using If statement & WHILE LOOP-----------")
n=int(input("How many numbers??? : "))
f1=0
f2=1
c=2
if n==1:
    print(f1)
elif n==2:
    print(f1,'\n',f2)
else:
    print(f1,'\n',f2)
while c<n:
    f=f1+f2
    print(f)
    f1,f2=f2,f
    c+=1
