# Haz como en el ejercicio anterior, pero esta vez acepta clientes en paralelo, los que hagan falta.

import socket
import threading

# La funcion de controlar cliente, tiene el socket y su ip y envia al cliente ese saludo y luego cierra su conexion
def controlar_cliente(client_socket, addr):
    print(f'Cliente conectado desde {addr}')
    # Se envia el mensaje
    client_socket.sendall(b'Hola, cliente!\n')
    # Cerramos el socket del cliente 
    client_socket.close()


# Crear socket de servidor. #AF_INET -> familia ip, transmisión en stream mediante TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Ahora despues de crear el socket, lo vinculamos a una direccion y puerto
server_socket.bind(('127.0.0.1', 8081))
print('Servidor esperando conexiones en el puerto 8081')
#Poner el socket en modo escucha
server_socket.listen()
print('El servidor esta esperando conexiones')
try:
    while True:
        # El addr añade la direccion del cliente que se conecta
        client_socket, addr = server_socket.accept()
        # Crear un hilo para manejar al cliente, por que con eso es como se puede hacer en paralelo
        hilo_conexion = threading.Thread(target=controlar_cliente, args=(client_socket, addr))
        hilo_conexion.start()

except socket.error as exc:
	print(f"Excepción de socket: {exc}")
finally:
    # Cerramos el socket del servidor
    server_socket.close()
    print('Servidor cerrado.')

