# Programa que hace la hipotenusa
# Las variables de a y b son las longitudes de los catetos.

# Primero cogemos las variables
cateto_a = float(input("Introduce el valor del cateto a: "))
cateto_b = float(input("Introduce el valor del cateto b: "))

# Y se calcula la hipotenusa usando el teorema de pitagoras
calc_hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5 #0.5 es la expresion matematica de la raiz cuadrada

# Y ahora se muestra el resultado en pantalla
print("La hipotenusa es:", calc_hipotenusa)
