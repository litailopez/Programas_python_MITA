"""Crear un diccionario de llave numérica dias, con los siguientes elementos:
1 - Lunes, 2 - Martes, 3 - Miércoles, 4 - Jueves, 5 - Viernes, 6 - Sabado, 7 - Domingo.
• Muestre el diccionario.
• Luego, accede y muestra:
o El primer elemento usando []
o El último elemento usando []
o El quinto elemento usando get()
o El séptimo elemento usando get()
o Muestre el diccionario completo."""


import os
os.system('cls')
Dias = {
    '1':'Lunes',
    '2':'Martes',
    '3':'Miercoles',
    '4':'Jueves',
    '5':'Viernes',
    '6':'Sabado',
    '7':'Domingo'
}

print(f'\nEl diccionario original: \n{Dias}\n')
print('Primer elemento: ', Dias['1'])
print('Ultimo elemento: ', Dias['7'])
print('Quinto elemento: ', Dias.get('5'))
print('Septimo elemento: ', Dias.get('7'))
print(f'\nDiccionario completo: \n{Dias}')

