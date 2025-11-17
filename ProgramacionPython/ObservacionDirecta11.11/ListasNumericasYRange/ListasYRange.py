# 4. Listas numéricas y función range (2 punto)
# a) Crea una lista de números del 1 al 20 usando la función range. (0,6 puntos)
# b) Genera una lista con los múltiplos de 3 entre 1 y 30. (0,6 puntos)
# c) Muestra los números pares de la lista usando slicing. (0,8 puntos)

# a) Creamos una lista de números del 1 al 20 usando la función range
numeros_1_a_20 = list(range(1, 21)) 
print("Lista de números del 1 al 20:", numeros_1_a_20)

# b) Generamos una lista con los múltiplos de 3 entre 1 y 30
multiplos_de_3 = list(range(3, 31, 3))
print("Lista de múltiplos de 3 entre 1 y 30:", multiplos_de_3)

# c) Mostramos los números pares de la lista usando slicing
numeros_pares = numeros_1_a_20[1::2]
print("Números pares de la lista del 1 al 20:", numeros_pares)