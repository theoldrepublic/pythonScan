import socket
#get the name of my computer
print(socket.gethostname())
#get the ip adress of this computer
print(socket.gethostbyname(socket.gethostname()))

