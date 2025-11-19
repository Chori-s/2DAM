# Modifica la función make_tshirt (“del ejercicio anterior”) para que las camisetas con
# tamaño L por defecto muestre el mensaje “I love Python” si no se especifica mensaje.
# Haz la llamada a make_shirt() para las camisetas con tamaño L y M y muestre su
# mensaje por defecto, y haz la llamada a make_shirt() de cualquier otro tamaño con un
# mensaje diferente.

def make_shirt(tamanio="L", mensaje="I love Python!"):
    print(f"Shirt with size: {tamanio}")
    print(f"Message to print: {mensaje}")

# Llamada a la función con tamaño L y mensaje por defecto
make_shirt()

# Llamada a la función con tamaño M y mensaje por defecto
make_shirt(tamanio="M")

make_shirt(tamanio="L")

# Llamada a la función con tamaño XS y mensaje personalizado
make_shirt(tamanio="XS", mensaje="Wonderful!")

# Llamada a la función con tamaño S y mensaje personalizado
make_shirt(tamanio="S", mensaje="Happiness!")

