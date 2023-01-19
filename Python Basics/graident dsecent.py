import numpy as np

def gradient_decent(x,y):
    m_curr = b_curr = 0
    iterations =10000
    n = len (x)
    learning_rate= 0.0001
    for i in range(iterations):
        yp= m_curr * x + b_curr

        cost = (1/n) * sum([val**2 for val in (y-yp)]) #This is mean squared fomula
        md  = -(2/n) * sum(x*(y-yp)) # this is the dy/dm
        bd  = -(2/n) * sum(y-yp)     #this is the dy/db
        m_curr =m_curr -learning_rate *md
        b_curr =b_curr -learning_rate *bd

        print(" m {} , b {} , cost {}, iteration {} ".format(m_curr,b_curr,cost,i))
#
# x=np.array([1,2,3,4,5])
# y=np.array([5,7,9,11,13])

x= np.array([92,56,88,70,80,49,65,35,66,67])
y= np.array([98,68,81,80,83,52,66,30,68,73])

gradient_decent(x,y)
