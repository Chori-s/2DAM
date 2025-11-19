# Situacion mas real, en el semaoro pueden pasar varios coches a la vez y peatones tambien, pero no pueden pasar a la vez peatones y coches
# Hazlo como en el ejercicio anterior, usando solo los conceptos que vimos hasta ahora (hilos, semaforos, locks, eventos, time.sleep)

import threading
import time
import random

class Cruce:
    def __init__(self):
        self.semaforo_coches = threading.Condition()
        self.peatones_cruzando = 0
        self.peatonesEnCruce=[]
        self.cochesEnCruce=[]
        self.coches_cruzando = 0

def coche(numCoche, cruce):
    print(f"Coche {numCoche} intentando cruzar el cruce.")
    with cruce.semaforo_coches:
        while cruce.peatones_cruzando > 0:
            cruce.semaforo_coches.wait()
        cruce.coches_cruzando += 1
        cruce.cochesEnCruce.append(numCoche)
        print(f"Coche {numCoche} cruzando el cruce. Coches en cruce: {cruce.cochesEnCruce}")
    tiempo_cruce = random.uniform(1, 3)
    time.sleep(tiempo_cruce)
    with cruce.semaforo_coches:
        cruce.coches_cruzando -= 1
        cruce.cochesEnCruce.remove(numCoche)
        print(f"Coche {numCoche} ha cruzado el cruce. Coches en cruce: {cruce.cochesEnCruce}")
        if cruce.coches_cruzando == 0:
            cruce.semaforo_coches.notify_all()