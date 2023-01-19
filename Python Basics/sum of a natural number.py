num=int(input('ENTER A NUMBER: '))
if num<0:
    print('Enter a positive number:')
else:
    # sum=0
    # while(num>0):
    #     sum+=num
    #     num-=1
    sum=num*((num+1)/2)
    print('The sum is ',+-sum)
