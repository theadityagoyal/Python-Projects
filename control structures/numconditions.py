"""Given an integer, n , perform the following conditional actions:

1)If is odd, print Weird and odd
2)If is even and in the inclusive range 2 to 5 , print Not Weird
3)If is even and in the inclusive range of 6 to 20 , print Weird from 6 and above 6
4)If is even and greater than 20 , print even and not Weird above 20"""




num = int(input("enter the number of your choice"))
if num % 2 == 1:
    print("Weird and odd")
elif num % 2 == 0 and 2 <= num <= 5:
    print("Not Weird between 2 and 5")
elif num % 2 == 0 and 6 <= num <= 20:
    print("Weird from 6 and above 6")
elif num%2==0 and num>20:
    print("even and not Weird above 20")
