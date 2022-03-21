#improtamos socket

import socket
import json

#Creando un socket para el cliente
c = socket.socket()

#conectando con el servidor en este caso es el "localhost" y el mismo puerto "8081"
c.connect(('localhost', 9000))

#preguntado al cliente para que ingrese elñ numero de cuenta y el monto a enviar
cuenta = input("Ingrese el numero de su cuenta: ")
monto = input("Ingrese el monto a enviar: ")
info = [str(cuenta), str(monto)]

info = json.dumps(info)
c.send(bytes(info, 'utf-8'))

#convirtiendio el mensaje recibido de formato "bytes" a "string" con: " -decode()"
print(c.recv(1024).decode())