import cmath
print('QUADRATIC EQUATION!')

print('The standerd Quadratic equation is ax2+bx+c=0')
a=int(input('Enter the cofficient of a '))
b=int(input('Enter the cofficient of b '))
c=int(input('Enter the cofficient of c '))

d=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)

print('The roots are!')
print(root1,root2)