import socket

host='localhost'
port=5000

#create a client side socket using TCP/IP
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect it to server and port number using connect() method
s.connect((host,port))

#receive message string from server we use recv() method, at a time 1024 B
msg=s.recv(1024)

#repeat as long as message strings are not empty
while msg:
    print('Received: '+msg.decode())
    msg=s.recv(1024)

s.close()
