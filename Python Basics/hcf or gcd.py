# def compute_hcf(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller + 1):
#         if (x % i == 0) and (y % i == 0):
#             hcf = i
#     return hcf

def computeHCF(x,y):
    while(y):
        x,y=y,x % y
    return x

num1 = int(input('Enter first number: '))
num2 = int(input('Enter Second number: '))

print('The HCF of', num1, 'and', num2, 'is',computeHCF(num1, num2))

