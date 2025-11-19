import threading
import time

evento = threading.Event()

class Carlos(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while not evento.is_set():
            time.sleep(0.5)
            print("Holaaa zoi kharlos")

        print("Adiozz zigo ziendo kharlos")

class noah(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Olaa ke dize karlos")
        evento.set()


elCarlos = Carlos()
elCarlos.start()

time.sleep(2)

elNoah = noah()
elNoah.start()

elCarlos.join()
elNoah.join()

print("Programa terminado")