#a TCP/IP server that sends messages to client
import socket

#take the server name and port number
host='localhost'
port=5000

#create a socket at server side using TCP/IP protocol
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket with server and port number
s.bind((host,port))

#allow maximum 1 connection to the socket
s.listen(1)

#wait till a client accepts connection, c is connection object and addr is address of client that has accepted connection
c,addr=s.accept()

#display client address
print("connection from: ",str(addr))

#send messages to the client after encoding into binary string
c.send(b"Hello client, how are you")
msg="Bye!"
c.send(msg.encode())  #other way to convert string into a binary format using encode() method

#disconnect the server
c.close()

