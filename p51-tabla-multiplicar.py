# tabla de multiplicar con for

import os

while(True):
    os.system('cls')
    
    t = int(input('Que tabla deseas ? '))
    n = int(input('Hasta donde la deseas ? '))
    
    for i in range(1, n+1):
        print(f'{t} x {i} = {t*i}')

    res = input('\n\nDeseas continuar (S/N) ? ').upper()
    if res=='N':
        break