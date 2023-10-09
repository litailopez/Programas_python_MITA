# Nombres y edades

import os
os.system('cls')
datos = {}
print('Introduce nombres y edades *en el nombre para terminar')
while True:
    nombre = input('Dame el nombre: ')
    if nombre!='*':
        datos[nombre]=int(input('Edad: '))
    else:
        break

print(f'\n\nLos datos introducidos son: \n{len(datos)} - {datos}\n')
  
s=p=0
for n,e in datos.items():
    print(f'{n:<10} - {e:3}')
    s= s + e
    p = s /len(datos)
        
print(f'\n\nLa suma: {s} y el promedio es: {s/len(datos)}')