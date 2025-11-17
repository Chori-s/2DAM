""" 
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.
"""
Nombres = ["Carlos", "Samu", "Mario"];

print('Queridos comensales,', Nombres[0], 'no podra acudir a la cena de mañana')

Nombres[0] = 'Jorge'

print('Asi que el nuevo invitado sera,', Nombres[0], 'enviare las invitaciones de nuevo para que las tengais actualizadas')
print('Querido', Nombres[0], 'estas invitado a una cena en mi casa el proximo dia')
print('Querido', Nombres[1], 'estas invitado a una cena en mi casa el proximo dia')
print('Querido', Nombres[2], 'estas invitado a una cena en mi casa el proximo dia')

