"""Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir
0. El proceso debe poder repetirse hasta que el usuario lo decida."""

import os

while(True):

    cuenta = mayor = 0 
    os.system('cls')

    while(True):
        num = int(input("Numero? "))
        if num != 0:
            cuenta = cuenta + 1
            if num >= mayor:
                mayor = num
            else:
                continue
        else:
            break

    print(f"El numero mayor es {mayor}")
 
    
    res = input("\nDeseas continuar (S/N)?: ").upper()
    if res == "N": break

print("\nProceso terminado")
