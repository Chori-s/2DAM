# Haz una lista que contenga una serie de mensajes breves. Pasa la lista a una función
# llamada show_messages(), que imprima cada mensaje de texto en la lista.
# La lista contendrá los mensajes: email John, buy flowers, complete tutorial y buy food.


def show_messages(mensaje):   
    for message in mensaje:
        print(f"message: {message}")
mensaje = ["email John", "buy flowers", "complete tutorial", "buy food"]
show_messages(mensaje)