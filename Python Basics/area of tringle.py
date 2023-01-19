a=int(input('Enter the side of a '))
b=int(input('Enter the side of b/n'))
c=int(input('Enter the side of c/n'))
s=int(((1/2)*(a+b+c))) #semi perimeter
area=(s*(s-a)*(s-b)*(s-c))**0.5#area of triangle

print('The area of triangle is ',area)