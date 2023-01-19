




"""f=open('myfile.txt','w')
print('Enter text (@ at the end): ')
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str+"\n")

f.close()"""





















"""f=open('myfile.txt','r')
print('the file contents are :')
str=f.read()
#print(str)
#f.read()
#f.readlines()# displays all strings as list elements
f.read().splitlines() #for suppressing \n 
f.close()"""














f=open('myfile.txt','a+')
print('enter text to append :')
while str!='@':
    str=input()

    if(str!='@'):
        f.write(str+"\n")
f.seek(20,0)  #f.seek(offset,fromwhere) offset is number of bytes to move, fromwhere 0 is beg, 1 is curr and 2 is end

print('The file contents are :')
str=f.read()
print(str)

f.close()










