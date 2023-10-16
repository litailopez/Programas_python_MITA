"""Crear un diccionario de llaves de cadena países, con los siguientes elementos:
Argentina - 100, Brasil - 200, Colombia - 300, Chile - 400, Ecuador - 500, Bolivia - 600, Jamaica - 700.
• Muestre el diccionario.
• Después modifique elementos como sigue:
o Modifique la llave Brasil por 250 usando []
o Modifique la llave Chile por 450 usando []
o Modifique la llave Bolivia por 650 usando update()
o Modifique la llave Jamaica por 750 usando update()"""

import os
os.system('cls')
Paises = {
    'Argentina':'100',
    'Brasil':'200',
    'Colombia':'300',
    'Chile':'400',
    'Ecuador':'500',
    'Bolivia':'600',
    'Jamaica':'700'
}

print(f'\nEl diccionario original: \n{Paises}\n')
Paises['Brasil'] = '250'
Paises['Chile'] = '450'
Paises.update({'Bolivia':'650'})
Paises.update({'Jamaica':'750'})

print(f'\nEl diccionario nuevo: \n{Paises}\n')