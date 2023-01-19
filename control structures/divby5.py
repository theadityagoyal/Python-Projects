# create a list and print the numbers divisible by 5 till the number==150


list of 10 nos.

print only the nos, divisible by 5

break the execution when the no. 150 is encountered


[1, 30, 45, 66, 75, 90, 150, 130, 140, 199]




























list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list1:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)
