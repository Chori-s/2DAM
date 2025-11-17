""" 
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

Nombres = ["Jorge", "Samu", "Mario"];

print(Nombres,'He encontrado una mesa mas grande, asi que invitaremos a 3 mas')

Nombres.insert(0, 'marcoS')
Nombres.insert(len(Nombres) //2, 'Iker')
Nombres.append('Nacho')

print('Querido', Nombres[0], 'estas invitado a una cena en mi casa el proximo dia')
print('Querido', Nombres[1], 'estas invitado a una cena en mi casa el proximo dia')
print('Querido', Nombres[2], 'estas invitado a una cena en mi casa el proximo dia')
print('Querido', Nombres[3], 'estas invitado a una cena en mi casa el proximo dia')
print('Querido', Nombres[4], 'estas invitado a una cena en mi casa el proximo dia')
print('Querido', Nombres[5], 'estas invitado a una cena en mi casa el proximo dia')
