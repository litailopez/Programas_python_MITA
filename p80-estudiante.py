# Estudiante

import os
os.system('cls')
estudiante = {
    'nombre':'Juan Perez',
    'edad':45,
    'correo':'jperez@msn.com',
    'carrera':'Sistemas'
}
print(f'\nEl diccionario original: \n{estudiante}')
estudiante['calificacion'] = 9.5
estudiante['correo']='juanp@gmail.com'
print(f'\nEl diccionario actualizado: \n{estudiante}')

print('\nLas llaves: ')
for k in estudiante.keys():
    print(k, end=", ")

print('\n\nLos valores: ')
for v in estudiante.values():
    print(v, end=", ")

print("\n\nLlaves y valores:\n")
for k,v in estudiante.items():
    # :<10 es alineado a la derecha en 10 posiciones
    print(f'{k:<10} : {v}')