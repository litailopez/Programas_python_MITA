# imprimir numeros de uno a 1 o de n a 1, según el usuario lo decida

import os 

while(True):
    os.system('cls')

    print("[1] Imprimir numeros 1 a n")
    print("[2] Imprimir numeros n a 1")

    op=int(input("Elije: "))

    if op == 1:
        print("Imprimiendo de 1 hasta n\n")
        n = int(input("Dame el valor de n"))
        for z in range (1, n+1, 1):
            print(z, end=" ")

    elif op == 2:
        print("Imprimiendo de n hasta 1\n")
        n = int(input("Dame el valor de n"))
        for z in range (n, 0, -1):
            print(z, end=" ")
    else:
        print("Opcion invalida")
        
    res = input("\nDeseas continuar (S/N)?: ").upper()
    if res == "N": break


print("\nProceso terminado")