#importamos socket
import socket
import json

mi_socket = socket.socket()
mi_socket.connect(('localhost',9000))

print(mi_socket.recv(1024).decode())
#preguntado al cliente para que ingrese elñ numero de cuenta y el monto a enviar
cuenta = input("Ingrese el numero de su cuenta: ")
monto = input("Ingrese el monto a enviar: ")
info = [str(cuenta), str(monto)]

info = json.dumps(info)
mi_socket.send(bytes(info, 'utf-8'))

#convirtiendio el mensaje recibido de formato "bytes" a "string" con: " -decode()"
print(mi_socket.recv(1024).decode())