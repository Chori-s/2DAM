# Usando un programa que escribistes (ejemplos usados anteriormente en el capítulo),
# almacena una función en un archivo separado. Importa la función en tu archivo de
# programa principal, y llama a la función usando cada uno de los siguientes
# procedimientos:
# Mostrar un ejemplo de cada uno (usar distintos nombres para poder hacer uso de la
# importación de dicha función al fichero principal de tu aplicación).
# Ejemplo de uso con la función build_profile()
# Resultado de la pantalla de ejecución. ( imports sobre funcionaes de user_profile())

# Aqui se importan las funciones de los otros ejercicios
# Aqui se imprime el resultado de cada uno de los ejercicios que he importado sin cambiar nada

from printing_functions import print_models, show_completed_models

print("")
print("Ejercicio de build profile:")
from Ejercicio7 import build_profile

print("")
print("Ejercicio de describe city:")
from Ejercicio3 import describe_city

# Aqui ejecuto la funcion importada con los datos del ejercicio9
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Y aqui los imprimo
print("")
print("Ejercicio de printing functions:")
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Ejecutamos por aqui tambien la funcion del ejercicio7
print("")
print("Ejercicio de build profile:")
user_profile = build_profile('Benalmádena', 'Informatica', 'ivan@gmail.com', 'Onix', 'Iván', 'Liñán')
print(user_profile)

# Ejecutamos por aqui tambien la funcion del ejercicio3
print("")
print("Ejercicio de describe city:")
describe_city('Santiago', 'Chile')
describe_city('Paris', 'Francia')
describe_city('Tokio', 'Japon')


