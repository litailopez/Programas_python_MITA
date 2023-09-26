# imprime pares e impares y su suma en el rango de n

import os

while(True):
    os.system('cls')
    print('Pares e impares de 1 a n y su suma \n')
    n = int(input('Hasta donde deseas los numeros? '))
    s = 0
    print("\nNumeros pares y su suma:")
    for par in range(2,n+1,2):
        print(par,end=' ')
        s = s + par
        print(f'\nSuma pares: {s}')
    
    s = 0
    print("\nNumeros impares y su suma:")
    for impar in range(1,n+1,2):
        print(impar,end=' ')
        s = s + impar
        print(f'\nSuma impares: {s}')
    res = input("\nDeseas continuar (S/N)?: ").upper()
    if res == "N": break
    
print('\nPrograma terminado')