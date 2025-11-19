# (Uso de eventos) Un hilo prepara datos y otros hilos esperan a que los datos esten listos para procesarlos

import threading
import time
import random

def preparadorDatos(evento, datos):
    print("Preparando datos")
    with evento:
        tiempo_preparacion = random.uniform(2, 5)
        time.sleep(tiempo_preparacion)
        datos.extend([random.randint(1, 100) for _ in range(5)])
        print("Datos preparados:", datos)
        evento.notify_all()

def procesadorDatos(evento, datos, numProcesador):
    print(f"Procesador {numProcesador} esperando a que los datos estén listos.")
    with evento:
        evento.wait()
        print(f"Procesador {numProcesador} procesando datos: {datos}")
        tiempo_procesamiento = random.uniform(1, 3)
        time.sleep(tiempo_procesamiento)
        print(f"Procesador {numProcesador} ha terminado de procesar los datos.")

evento = threading.Condition()
datos = []
preparador = threading.Thread(target=preparadorDatos, args=(evento, datos))
procesadores = [threading.Thread(target=procesadorDatos, args=(evento, datos, i)) for i in range(3)]
preparador.start()
for p in procesadores:
    p.start()
preparador.join()
for p in procesadores:
    p.join()
print("Todos los datos han sido procesados.")
