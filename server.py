import socket

#Create Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding a socket to an address and port
server_socket.bind(('localhost', 7777))

#Waiting for connections
server_socket.listen(1)
print("Waiting for connections...")

#Connect
client_socket, client_address = server_socket.accept()
print("Connection with", client_address)

#Data receive cycle
while True:
    #data recieve
    data = client_socket.recv(1024)
    if data:
         print(data.decode('utf-8'))

    else:
        break
