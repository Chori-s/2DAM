# El servidor genera un número secreto aleatorio (por ejemplo, entre 1 y 100). Un cliente se conecta y envía intentos. 
# El servidor responde si el número es:
# "Muy alto"
# "Muy bajo"
# "Correcto”
# El cliente sigue enviando intentos hasta acertar.

import socket
import random
import threading

#Primero creamos una funcion para manejar al cliente
def manejar_cliente(client_socket, addr, numero_secreto):
    print(f'Cliente conectado desde {addr}')
    while True:
        # Aqui el servidor recibe desde el socket del cliente el intento
        # recv es el tamaño del buffer para recibir datos, decode lo convierte a string y strip elimina espacios en blanco
        intento = client_socket.recv(1024).decode().strip()
        # Si no hay datos, sale del bucle
        if not intento:
            break  
        # Y ahora del string se pasa a int
        intento_num = int(intento)
        
        # Y ahora comparo el intento con el numero secreto del servidor
        if intento_num < numero_secreto:
            client_socket.sendall(b'Muy bajo\n')
        elif intento_num > numero_secreto:
            client_socket.sendall(b'Muy alto\n')
        else:
            client_socket.sendall(b'Correcto\n')
            break  # Y con esto salgo del bucle si acierta
    
    client_socket.close()
    print(f'Conexión con {addr} cerrada.')

# Crear socket de servidor. AF_INET -> IPv4, SOCK_STREAM -> TCP, para que se ejecute
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
# Vincular el socket a una dirección y puerto
server_socket.bind(('127.0.0.1', 8081))
print('Servidor esperando conexiones en el puerto 8081')    

# Poner el socket en modo escucha
server_socket.listen()
print('El servidor está esperando conexiones')  
try:
    while True:
        # Aceptar conexión de un cliente
        client_socket, addr = server_socket.accept()
        # Generar un número secreto aleatorio entre 1 y 10 para cada cliente
        numero_secreto = random.randint(1, 10)
        # Crear un hilo para manejar al cliente como antes
        hilo_conexion = threading.Thread(target=manejar_cliente, args=(client_socket, addr, numero_secreto))
        hilo_conexion.start()

except socket.error as exc:
    print(f"Excepción de socket: {exc}")
finally:
    # Cerrar el socket del servidor
    server_socket.close()
    print('Servidor cerrado.')

