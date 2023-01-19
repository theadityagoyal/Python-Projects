"""def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = list(map(fahrenheit, temp))
C = list(map(celsius, F))
print(F)
print(C)"""



























"""map() can be applied to more than one list. The lists have to have the same length. map() will apply its lambda function to the elements of the argument lists,
i.e. it first applies to the elements with the 0th index, then to the elements
with the 1st index until the n-th index is reached:"""
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
d=list(map(lambda x,y,z:x+y+z, a,b,c))

print(d)


















