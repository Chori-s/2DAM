# 2. Slicing de listas (2 punto)
# a) Muestra los tres primeros elementos de una lista de números del 1 al 10. (0,6 puntos)
# b) Muestra los tres últimos elementos de esa lista. (0,6 puntos)
# c) Muestra los elementos del índice 4 al 7. (0,8 puntos)

# Creamos una lista de números del 1 al 10
numeros = list(range(1, 11))

# a) Mostramos los tres primeros elementos de la lista
primeros_tres = numeros[:3]
print("Los tres primeros elementos son:", primeros_tres)

# b) Mostramos los tres últimos elementos de la lista
ultimos_tres = numeros[-3:]
print("Los tres últimos elementos son:", ultimos_tres)

# c) Mostramos los elementos del índice 4 al 7
elementos_4_a_7 = numeros[4:8]
print("Los elementos del índice 4 al 7 son:", elementos_4_a_7)