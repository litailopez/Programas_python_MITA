"""Crear un diccionario de llave de cadena, ventas, con los siguientes elementos:
Juan - 1550, Jose - 2600, Maria - 2220
• Mostrar el diccionario
• Luego agregar los siguientes elementos al diccionario:
o Elemento Rocio - 2500 usando []
o Elemento: Mateo - 1567 usando []
o Elemento: Andrea - 9567 usando update()
o Elemento: Miguel - 1234 usando update()"""

import os
os.system('cls')
Nombres = {
    'Juan':'1550',
    'Jose':'2600',
    'Maria':'2220'
}

print(f'\nEl diccionario original: \n{Nombres}\n')

Nombres['Rocio'] = '2500'
Nombres['Mateo'] = '1567'
Nombres.update({'Andrea':'9567'})
Nombres.update({'Miguel':'1234'})

print(f'\nEl diccionario nuevo: \n{Nombres}\n')


