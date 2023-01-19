# num=int(input('Enter a number: '))
#
# fact=1
# if num < 1:
#     print('Factorial does not exist')
# elif num==0 or num==1:
#     print('Factorial is 1')
# else:
#     for i in range(1,num+1):
#         fact=fact*i
#     print('The Factorial of ',num,'is',fact)

def fact_recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact_recursion(n-1)
num=int(input('Enter a number: '))
print('Factorial of',num,'is',fact_recursion(num))