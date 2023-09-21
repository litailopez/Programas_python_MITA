"""Se desea imprimir los números pares desde 100 hasta el número que el usuario decida (n), además deberá
imprimirse la suma de esos números pares. El proceso debe poder repetirse hasta que el usuario lo decida."""

import os


while(True):
    os.system('cls')
    num = int (input("Hasta que numero menor a 100?: "))
    cont = 100
    n = 0

    while cont >= num:
        op = cont % 2
        if op == 0:
            print(cont, end = " ")
        
            n = n + cont
    
        cont = cont - 1
    print ("\nLa suma es : ", n)
    res = input("\nDeseas continuar (S/N)?: ").upper()
    if res == "N": break

print("\nProceso terminado")