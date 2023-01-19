def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)
nterms=int(input('Enter the number of terms: '))

if nterms<=0:
    print('Please Enter a positive number: ')
else:
    print('The sum of',nterms,'terms is',sum(nterms))