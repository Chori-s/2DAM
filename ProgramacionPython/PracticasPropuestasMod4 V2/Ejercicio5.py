# Comienza con una copia del ejercicio anterior (ejercicio 4).
# Llama a la función send_messages() con una copia de la lista de mensajes.
# Después de llamar la función send_messages(), imprime ambas listas de mensajes (lista
# messages y lista sent_messages) para asegurarte que los mensajes fueron movidos de
# lista correctamente.

def send_messages(mensajes, sent_messages): 
    while mensajes:
        current_message = mensajes.pop(0)
        print(f"message: {current_message}")
        sent_messages.append(current_message)
mensajes = ["buy food", "complete tutorial", "buy flowers", "email John"]
sent_messages = []
send_messages(mensajes[:], sent_messages)  
print("\nMessages sent -------------------")
print(f"messages: {mensajes}")
print(f"sent_messages: {sent_messages}")



