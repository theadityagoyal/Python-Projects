def computeLCM(x,y):
    if x>y:
        greater=x

    else:
        greater=y
    while(True):
        if (greater % x == 0) and (greater % y == 0):
            lcm=greater
            break
        greater+=1
    return lcm

num1 = int(input('Enter first number: '))
num2 = int(input('Enter Second number: '))

print('The HCF of', num1, 'and', num2, 'is',computeLCM(num1, num2))
