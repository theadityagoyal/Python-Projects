import socket
host='localhost'
port=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("connection from: ",str(addr))
c.send(b"Hello client , how are you")
msg="Bye!"
c.send(msg.encode())
c.close()
