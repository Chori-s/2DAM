# Escribe una función que almacene información de un coche en un diccionario. La
# función debería siempre recibir el nombre del fabricante y modelo. Debería recibir un
# número arbitrario de argumentos por palabra clave (keyword), tal como color y una
# característica opcional. La función debería ser llamada de la siguiente forma:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)

def build_car_profile(color, two_package, manufacturer, model, **car_profile):
    car_profile = {
        'manufacturer': manufacturer,
        'model': model,
        'color': color,
        'two_package': two_package
    }
    return car_profile

car = build_car_profile('blue', True, 'subaru', 'outback')
print(car)

car1 = build_car_profile('white', False, 'Honda', 'Civic')
print(car1)
    
