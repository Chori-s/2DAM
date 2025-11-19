# Escribe una función llamada make_shirt() que acepta el tamaño “XS,S,M,L,XL,XXL”
# y el texto de un mensaje que debería de ser impreso en la camiseta.
# La función debería imprimir una frase que resuma el tamaño de la camiseta y el mensaje
# impreso en ella.
# Llama a la función una vez usando argumentos posicionales para crear una camiseta.
# Llama a la función una segunda vez usando los argumentos por palabra clave
# (keywork).

def make_shirt(tamanio, mensaje):
    print(f"Shirt with size: {tamanio}")
    print(f"Message to print: {mensaje}")


# Llamada a la función con argumentos posicionales
make_shirt("M", "Hello!")

# Llamada a la función con argumentos por palabra clave
make_shirt(tamanio="XL", mensaje="This is great!")

  