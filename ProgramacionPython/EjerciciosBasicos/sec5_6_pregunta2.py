# Este programa convierte una cantidad de segundos que se le pase en horas, minutos y segundos.
# Permite al usuario introducir los segundos y muestra el resultado con el tiempo completo

# Primero pones los segundos totales
segundos_tot = int(input("Dime una cantidad de tiempo en segundos: "))

# Y luego se calcula los totales con sus variables, es decir, una hora tiene 3600 segundos, etc...
horas = segundos_tot // 3600
minutos = (segundos_tot % 3600) // 60
segundos = segundos_tot % 60

# Y ahora se muestra el resultado completo al usuario
print(f"Segun los segundos que me has dado, corresponde a lo siguiente: {horas} horas, {minutos} minutos y {segundos} segundos")

# Y ahora se muestra todo en el resultado del * segun las 9 veces que se repiten
print(f"{'*' * 9} {horas} : {minutos} : {segundos} {'*' * 9}")
