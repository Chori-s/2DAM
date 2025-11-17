""" 
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first
10 cubes.
"""

numero_al_cubo = [numero ** 3 for numero in range(1, 11)]
for cubo in numero_al_cubo:
    print(cubo)
