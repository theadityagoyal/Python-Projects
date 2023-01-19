num=int(input('Enter a number where you want a Fibonacci sequence Terms: '))
n1=0
n2=1
count=0

if num<=0:
    print('please enter a positive number:')
elif num==1:
    print('Fibonacci sequence upto ',num,':')
    print(n1)
else:
    print('Fibonacci sequence upto ', num, ':')
    while count<num:
        print(n1,end=' ,')
        nth=n1+n2
        n1=n2  #updated values
        n2=nth
        count=count+1

