#importamos socket
from asyncio import current_task
import socket
import json

#Creamos un socket para el servidor
s = socket.socket()
#mensaje que nos indica que se creo correctamente
print("Socket creado !!")

'''
    *********************************************************************************
    
    indicamos la ip y el puerto, puede ser le localhost o tu ip privada
    en este caso usare el "localhost" y el puerto "8081"
    
    *********************************************************************************
'''

s.bind(('localhost',9000))
s.listen(3)

#mensaje que indica que esta esperando conexiones
print("Esperando conexiones ./././")

while True:
    c, addr = s.accept()

#recibiendo el mesnaje nombre del cliente y tranformandolo en formato "bytes"
#a "string" con " -decode()"

    info = c.recv(1024).decode()
    info = json.loads(info)
    cuenta = info[0]
    monto = info[1]
    ip = addr[0]
    
    print("Conectando con: " + str(ip) + "Cuenta: " + str(cuenta) + " " + "Monto: " + str(monto))

#enviando mensaje en formato "byte" a los clientes
    c.send(bytes('Bienvenidos a mi servidor!!', 'utf-8'))