""" 
3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.
"""

videojuegos = ["Minecraft", "Fortnite", "Palworld", "Diablo IV", "Pes 2011"]
print("Lista principal sin modificaciones:")
print(videojuegos)
videojuegos.sort()
print("\nLista de videojuegos ordenada alfabéticamente:")
print(videojuegos)
videojuegos.sort(reverse=True)
print("\nLista de videojuegos ordenada en orden alfabético inverso:")
print(videojuegos)
videojuegos.reverse()
print("\nLista de videojuegos en orden inverso al original:")
print(videojuegos)
videojuegos.append("Tom Clancy's The Division 2")
print("\nLista de videojuegos después de agregar 'Tom Clancy's The Division 2':")
print(videojuegos)
videojuegos.insert(2, "Plant vs Zombies Replanted")
print("\nLista de videojuegos después de insertar 'Plant vs Zombies Replanted' en la posición 2:")
print(videojuegos)
videojuegos.remove("Pes 2011")
print("\nLista de videojuegos después de eliminar 'Pes 2011':")
print(videojuegos)
usando_pop = videojuegos.pop()
print(f"\nVideojuego eliminado con pop(): {usando_pop}")
print("Lista de videojuegos después de usar pop():")
print(videojuegos)
length = len(videojuegos)
print(f"\nNúmero total de videojuegos en la lista: {length}")
print("\nLista de videojuegos ordenada temporalmente:")
print(sorted(videojuegos))
print("\nLista original de videojuegos nuevamente:")
print(videojuegos)
print("\nNúmero total de videojuegos en la lista después de todas las operaciones:")
print(len(videojuegos))
