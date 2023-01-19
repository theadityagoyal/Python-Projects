f1=open('myimage.jpg','rb')
f2=open('new.jpg','wb')

bytes=f1.read()
f2.write(bytes)

f1.close()
f2.close()























with open('sample.txt','w') as f:
    f.write('i am a learner\n')
    f.write('python is interactive\n')

with open('sample.txt','r') as f:
    for line in f:
        print(line)












