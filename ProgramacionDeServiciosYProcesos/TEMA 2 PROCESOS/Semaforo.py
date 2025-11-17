import threading
import time
import random

class Cruce:
    def __init__(self):
        self.condition = threading.Condition()
        self.cruzando = False

def coche(numCoche, cruce):
    with cruce.condition:
        while cruce.cruzando:
            cruce.cruzando.wait()
        cruce.cruzando = True
    print(f"Coche {numCoche} está cruzando el cruce.")
    time.sleep(random.uniform(0.5, 2.0))  
    with cruce.condition:
        print(f"Coche {numCoche} ha cruzado el cruce.")
        cruce.cruzando = False
        cruce.condition.notify_all()

def peaton(numPeaton, cruce):
    with cruce.condition:
        while cruce.cruzando:
            cruce.condition.wait()
        cruce.cruzando = True
    print(f"Peatón {numPeaton} está cruzando el cruce.")
    time.sleep(random.uniform(0.5, 2.0))  
    with cruce.condition:
        print(f"Peatón {numPeaton} ha cruzado el cruce.")
        cruce.cruzando = False
        cruce.condition.notify_all()


cruce = Cruce()

#Crear e iniciar hilos
hilos = []  

for i in range(3):
    t = threading.Thread(target=coche, args=(i, cruce))
    hilos.append(t)
    t.start()

for i in range(3):
    t = threading.Thread(target=peaton, args=(i, cruce))
    hilos.append(t)
    t.start()
    
for t in hilos:
    t.join()