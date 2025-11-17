import threading
import time
import random

servidor = threading.Semaphore(3)

class cliente(threading.Thread):
    def __init__(self, numCliente):
        super().__init__()
        self.numero = numCliente

    def run(self):
        print(f"Cliente {self.numero} intentando conectarse al servidor.")
        with servidor:
            print(f"Cliente {self.numero} conectado al servidor.")
            tiempo_conexion = random.uniform(1, 5)
            time.sleep(tiempo_conexion)
            print(f"Cliente {self.numero} desconectándose del servidor ")

clientes = []
for cont in range(10):
    c = cliente(cont+1)
    c.start()
    clientes.append(c)

for hilo in clientes:
    hilo.join()

print("Todos los clientes atendidos.")