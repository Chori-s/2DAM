# Ejercicio 6: Crea un servidor no orientado a conexión que esté permanentemente escuchando en el puerto en vez de desconectarse. Hará lo siguiente:
# Un cliente se conecta, pregunta una frase y la manda al servidor.
# El servidor le contesta lo siguiente al cliente:
# Me has enviado la cadena ‘XXXXX’
# Envíame más, quiero más
# Y el cliente le vuelve a enviar otra frase más y así un “no parar”
# Crea el cliente para que se comunique con el servidor

import socket
import threading
import time

def manejar_cliente(client_socket, addr):
    print(f'Cliente conectado desde {addr}')
    try:
        while True:
            # Esto recibe la frase del cliente
            frase = client_socket.recv(1024).decode().strip()

            # Si no hay datos, salir del bucle para que no se quede ahi sin decir na
            if not frase:
                break  

            # Responde al cliente con la respuesta que tengo, por eso el encode y el sendall
            respuesta = f'Me has enviado la cadena \'{frase}\'\nEnvíame más, quiero más\n'
            client_socket.sendall(respuesta.encode())
        # Esto esta puesto para que no se quede el hilo colgado si el cliente se desconecta
    except Exception as e:
        print(f'Error con el cliente {addr}: {e}')
        # Y este finally es para cerrar la conexion del cliente cuando termine
    finally:
        client_socket.close()
        print(f'Conexión con {addr} cerrada.')

# Crear socket de servidor. AF_INET -> IPv4, SOCK_STREAM -> TCP (Copia y pega del ejercicio anterior)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a una dirección y puerto
server_socket.bind(('localhost', 8081))

# Escuchar conexiones entrantes
server_socket.listen()
print('El servidor está esperando conexiones en el puerto 8081')
try:
    while True:
        # Esto acepta una nueva conexión
        client_socket, addr = server_socket.accept()
        # Y como ya sabemos hacer hilos, creamos uno nuevo para manejar al cliente
        hilo_conexion = threading.Thread(target=manejar_cliente, args=(client_socket, addr))
        hilo_conexion.start()
        # El servidor sigue escuchando nuevas conexiones aqui infinitamente hasta que se le pare manualmente con Ctrl+C
except KeyboardInterrupt:
    print("\nServidor detenido manualmente.")

finally:
    server_socket.close()  
    print('Servidor cerrado.') 