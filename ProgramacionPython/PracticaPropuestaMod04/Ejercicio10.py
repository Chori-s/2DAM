""" 
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a
slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to
print the last three items in the list.
"""
numeros = list(range(1, 11))
print("Los primeros 3 numeros de la lista son:")
for numero in numeros[:3]:
    print(numero)
print("Los 3 numeros del medio de la lista son:")
for numero in numeros[4:7]:
    print(numero)
print("Los 3 ultimos numeros de la lista son:")
for numero in numeros[-3:]:
    print(numero)


