# printing_functions.py

def print_models(unprinted_designs, completed_models):
    """
    Simula la impresión de cada diseño, hasta que no quede ninguno.
    Mueve cada diseño a completed_models después de imprimirlo.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Muestra todos los modelos que se han impreso.""" 
    for completed_model in completed_models:
        print(completed_model)
