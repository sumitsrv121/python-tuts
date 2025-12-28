from socket import socket

server_socket = socket()

print("server socket created")


server_socket.bind(("localhost", 9999))

# supports 3 connections
server_socket.listen(3)
print("server socket listening")


while True:
    client_socket, client_address = server_socket.accept()
    name = client_socket.recv(1024).decode()
    print(f"accepted connection from {client_address} and name of client: {name}")
    client_socket.send(bytes("Hello, world!", "utf-8"))
    client_socket.close()
