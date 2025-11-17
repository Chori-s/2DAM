# 1. Manipulación básica de listas (2 punto)
# a) Crea una lista con 5 nombres de personas. (0,2 puntos)
# b) Añade dos nombres más a la lista. (0,2 puntos)
# c) Imprime todos los nombres usando un bucle for. (0,3 puntos)
# d) Elimina el tercer nombre de la lista y vuelve a mostrar la lista. (0,3 puntos)

# Añadimos los nombres a la lista 
# a)
nombres = ["Carlos", "Iván", "Nacho", "Mario", "Iker"]

# Añadimos dos nombres más a la lista
# b)
nombres.append("marcoS")
nombres.append("Pepe Viyuela")

# Imprimimos todos los nombres usando un bucle for
# c)
print("\nLista de nombres:")
for nombre in nombres:
    print(nombre)

# Eliminamos el tercer nombre de la lista y volvemos a mostrar la lista
# d)
nombres.pop(2) 
print("\nLista de nombres después de eliminar el tercero:")
for nombre in nombres:
    print(nombre)
