# 5. List comprehensions (1 punto)
# a) Crea una lista de los cuadrados de los 10 primeros números naturales
# usando list comprehension. (0,4 puntos)
# b) Genera una lista de cubos entre 1 y 10 con list comprehension. (0,3 puntos)
# c) Muestra ambas listas. (0,3 puntos)

# a) Creamos una lista de los cuadrados de los 10 primeros números naturales
cuadrados = [x**2 for x in range(1, 11)]

# b) Generamos una lista de cubos entre 1 y 10 con list comprehension
cubos = [x**3 for x in range(1, 11)]

# c) Mostramos ambas listas
print("Lista de cuadrados de los 10 primeros números naturales:", cuadrados)
print("Lista de cubos entre 1 y 10:", cubos)
