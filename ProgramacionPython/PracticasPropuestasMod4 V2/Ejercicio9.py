# este ejercicio es el que se ejecuta por que tiene el import de la clase printing_functions.py

from printing_functions import print_models, show_completed_models

# Primera parte del código, diseño de modelos
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Uso las funciones importadas para imprimir los modelos y mostrar los completados
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
