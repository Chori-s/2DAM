# Acepta 5 clientes y después acaba

import socket

# Crear socket de servidor. AF_INET -> IPv4, SOCK_STREAM -> TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a una dirección y puerto
server_socket.bind(('127.0.0.1', 8081))
print('Servidor esperando conexiones en el puerto 8081')

# Poner el socket en modo escucha con una cola de 5 conexiones
server_socket.listen(5)

try:
    # Bucle para aceptar 5 clientes como máximo
    for i in range(5):
        # Acepto la conexión de un cliente
        client_socket, addr = server_socket.accept()
        print(f'Cliente conectado desde {addr}')

        # Enviar mensaje al cliente
        client_socket.sendall(b'Hola, cliente!\n')

        # Cerrar conexión del cliente
        client_socket.close()
        print('El servidor está esperando conexiones...')

except socket.error as exc:
    print(f"Excepción de socket: {exc}")

# Cerrar el socket del servidor
server_socket.close()
print('Servidor cerrado, ya ha aceptado a 5 clientes')
