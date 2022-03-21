#importamos socket
import socket
import json

mi_socket = socket.socket()
mi_socket.bind(('localhost',9000))
mi_socket.listen(5)
print("Esperando conexiones ./././")
while True:
    conexion, addr = mi_socket.accept()
    conexion.send(bytes('Bienvenido al servidor, ingrese la información.', 'utf-8'))
    '''
    ******************************************************************************
    
    
    
    ******************************************************************************
    '''
    ip = addr[0]
    print ("Nueva conexion establecida! con: " + ip)
    info = conexion.recv(1024).decode()
    info = json.loads(info)
    cuenta = info[0]
    monto = info[1]
    
    print("Conectando con: " + str(ip) + "Cuenta: " + str(cuenta) + " " + "Monto: " + str(monto))
    conexion.send(bytes('Información registrada.', 'utf-8'))
        
    conexion.close()