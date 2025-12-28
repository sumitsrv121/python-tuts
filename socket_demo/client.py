from socket import socket

client_socket = socket()


client_socket.connect(("localhost", 9999))

name = input("Enter your name: ")
client_socket.send(bytes(name, "utf-8"))

data = client_socket.recv(1024)

print(data.decode())
