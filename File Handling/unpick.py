import Emp1,pickle
f=open('Emp1.dat','rb')
print('Employee details: ')

while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print('End of file reached...')
        break
f.close()
