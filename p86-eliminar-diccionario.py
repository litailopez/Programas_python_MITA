"""Cree un diccionario de llave de cadena municipios con los siguientes elementos:
Apozol - 1863, Calera - 1868, Fresnillo - 1554, Guadalupe - 1821, Jalpa - 1824, Jerez - 1824, Loreto - 1931,
Mazapil - 1824, Momax - 1857.
• Mostrar el diccionario
• Eliminar los elementos siguientes, en cada operación mostrar el diccionario:
o Llave Apozol usando del
o Llave Fresnillo usando pop()
o Llave Momax usando popitem()
o Borrar todos los elementos del diccionario con clear()
• Mostrar diccionario."""

import os
os.system('cls')
Municipios = {
    'Apozol':'1863',
    'Calera':'1868',
    'Fresnillo':'1554',
    'Guadalupe':'1821',
    'Jalpa' : '1824', 
    'Jerez' : '1824', 
    'Loreto' : '1931',
    'Mazapil' : '1824', 
    'Momax' : '1857'
}

print(f'\nEl diccionario original: \n{Municipios}\n')

del Municipios['Apozol']
print(f'\nEl diccionario: \n{Municipios}\n')
Municipios.pop('Fresnillo')
print(f'\nEl diccionario: \n{Municipios}\n')
Municipios.popitem()
print(f'\nEl diccionario: \n{Municipios}\n')
Municipios.clear()
print(f'\nEl diccionario: \n{Municipios}\n')