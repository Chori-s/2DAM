# Ejercicio 1: Recibe una cadena del cliente y la devuelve en mayúsculas.
# El servidor le está preguntando constantemente.
# Si el servidor recibe el carácter ‘#’ se acaba el bucle 
# (Se desconecta el cliente) y el servidor se despide de él.

import socketserver
import threading

class Handler(BaseRequestHandler):
    def handle(self):
        print(f"Conexión establecida con {self.client_address}")
        while True:
            frase = self.request.recv(1024).strip()

            if not frase:
                break
            
            print(f"Recibido de {self.client_address}: {message}")
            if message == '#':
                self.request.sendall(b"Desconectando. ¡Adiós!\n")
                print(f"Desconectando a {self.client_address}")
                break
            response = message.upper().encode('utf-8')
            self.request.sendall(response)