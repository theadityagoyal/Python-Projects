def recursion_fibo(n):
    if n<=1:
        return n
    else:
        return(recursion_fibo(n-1)+recursion_fibo(n-2))
nterms=int(input('Enter the number of terms: '))

if nterms<=0:
    print('Please Enter a positive number: ')
else:
    print('Fibbonaci sequence :')
    for i in range(nterms):
        print(recursion_fibo(i),end=' ,')