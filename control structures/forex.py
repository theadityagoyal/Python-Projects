#FOR LOOP
print("--Multiplication table using FOR loop--")
n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"X",i,"=",n*i)
print("")
print("--Pascal triangles--")
n=int(input("Enter the rows:"))
trow=[1]
y=[0]
for x in range(max(n,0)):
    print((trow))
    trow=[l+r for l,r in zip(trow+y, y+trow)]
    n>=1
