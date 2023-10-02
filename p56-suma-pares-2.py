#Se desea imprimir los pares de 2 a n y su suma

import os

os.system('cls')

n = int(input('Hasta donde deseas los numeros? '))
s = 0
for par in range(2,n+1,2):
    print(par,end=' ')
    s = s + par
print(f'\nLa suma es: {s}')