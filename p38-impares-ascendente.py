""" Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n),
además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse hasta que el
usuario lo decida."""

import os


while(True):
    os.system('cls')
    num = int (input("Hasta que numero?: "))
    cont = 1

    while cont <=num:
        op = cont % 2
        if op != 0:
            print(cont, end = " ")
        cont = cont + 1
    res = input("\nDeseas continuar (S/N)?: ").upper()
    if res == "N": break

print("\nProceso terminado")