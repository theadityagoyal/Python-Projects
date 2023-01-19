# a UDP server that sends messages to client
import socket
import time

#take the server name and port number
host='localhost'
port=5000

#create a socket at server side to use UDP protocol
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#let the server wait for 5 seconds
time.sleep(5)

#send messages to the client after encoding into binary string
s.sendto(b"Hello client, how are you",(host,port))
msg="Bye!"
s.sendto(msg.encode(),(host,port))

#disconnect the server
s.close()
