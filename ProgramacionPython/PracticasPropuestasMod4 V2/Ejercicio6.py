# Escribe una función que acepte una lista de ingredientes que una persona quiere para su
# sándwich. La función debería tener un parámetro que recoja tantos ingredientes que
# sean suministrados en la llamada a la función, y debería imprimir un resumen con los
# ingredientes del sándwich pedido.
# Llama a la función 3 veces, usando un número diferente de argumentos cada vez para
# pedir el sándwich.

def hacer_Bocata(ingredientes):
    print("Haciendo un peazo de bocadillo con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")
hacer_Bocata(['mayonesa', 'atun', 'lechuga', 'jamon']) 

hacer_Bocata(['jamon', 'queso']) 

hacer_Bocata(['queso', 'bacon', 'lechuga'])