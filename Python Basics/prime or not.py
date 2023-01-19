# # take input from the user
# num = int(input("Enter a number: "))
#
# # prime numbers are greater than 1
# if num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")
#
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")


# import math
# # take input from the user
# num = int(input("Enter a number: "))
#
# # prime numbers are greater than 1
# if num > 1:
#    # check for factors
#    for i in range(2,math.ceil(num/2)):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")
#
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")




lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num,end=' , ')























