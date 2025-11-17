# 3. Copiar listas (2 punto)
# a) Define una lista con tus comidas favoritas. (0,4 puntos)
# b) Haz una copia de la lista y añádele una comida distinta. (0,8 puntos)
# c) Demuestra que son listas diferentes añadiendo elementos a ambas y mostrando el resultado. (0,8 puntos)

# a) Definimos una lista con nuestras comidas favoritas
comidas_favoritas = ["Pizza", "Sushi", "Tacos", "Pasta", "Ensalada"]

# b) Hacemos una copia de la lista usando slicing y le añadimos una comida distinta
comidas_favoritas_copia = comidas_favoritas[:]
comidas_favoritas_copia.append("Hamburguesa")

# c) Demostramos que son listas diferentes añadiendo elementos a ambas y mostrando el resultado
comidas_favoritas.append("Paella")
print("Lista original de comidas favoritas:", comidas_favoritas)
print("Copia de la lista de comidas favoritas:", comidas_favoritas_copia)
print("")
comidas_favoritas_copia.append("Sopa")
print("Lista original de comidas favoritas después de añadir un elemento:", comidas_favoritas)
print("Copia de la lista de comidas favoritas después de añadir un elemento:", comidas_favoritas_copia)


