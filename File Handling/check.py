# import os, sys
# fname=input('enter the filename :')

# if os.path.isfile(fname):
#     f=open(fname, 'r')
# else:
#     print(fname+'does not exist')
#     sys.exit()

# cl=cw=cc=0 

# for line in f:
#     words=line.split()
#     cl+=1
#     cw+=len(words)
#     cc+=len(line)

# print('no. of lines: ',cl)
# print('no. of words: ',cw)
# print('no. of characters: ',cc)

# f.close()
f=open('myfile.txt',"a")
