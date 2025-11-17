# 6. Estadística básica con listas (1 punto)
# a) Calcula el mínimo, máximo y suma de una lista de números enteros. (0,3
# puntos)
# b) Crea una lista de 10 números aleatorios y realiza los cálculos. (0,3 puntos)
# c) Muestra los resultados en formato “El mínimo es X, el máximo es Y, la suma
# es Z”. (0,4 puntos)

import random

# Creamos una lista de números enteros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a) Calculamos mínimo, máximo y suma de la lista de números enteros
minimo = min(numeros)
maximo = max(numeros)
suma = sum(numeros)

print(f"Para la lista {numeros}:")
print(f"El mínimo es {minimo}, el máximo es {maximo}, la suma es {suma}.")  

# b) Creamos una lista de 10 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]

# c) Calculamos mínimo, máximo y suma de la lista de números aleatorios
minimo_aleatorios = min(numeros_aleatorios)
maximo_aleatorios = max(numeros_aleatorios)
suma_aleatorios = sum(numeros_aleatorios)

print(f"Para la lista {numeros_aleatorios}:")
print(f"El mínimo es {minimo_aleatorios}, el máximo es {maximo_aleatorios}, la suma es {suma_aleatorios}.")  
