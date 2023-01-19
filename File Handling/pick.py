import Emp1, pickle

f=open('Emp1.dat','wb')
n=int(input('how many employees?'))

for i in range(n):
    id=int(input('Enter id: '))
    name=input('Enter name: ')
    sal=float(input('Enter salary: '))

    e=Emp1.Emp1(id,name,sal)

    pickle.dump(e,f)
f.close()

