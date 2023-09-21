"""Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, luego mostrar
cuantos números fueron introducidos y la suma de estos. El proceso debe poder repetirse hasta que el usuario lo
decida."""

import os

while(True):

    cuenta = suma = 0 
    os.system('cls')

    while(True):
        num = int(input("Numero? "))
        cuenta = cuenta + 1
        suma = suma + num
        if suma >= 200:
            break

    print(f"Se introdujeron {cuenta} numeros")
    print(f"La suma de los numeros es {suma}")
    
    res = input("\nDeseas continuar (S/N)?: ").upper()
    if res == "N": break

print("\nProceso terminado")
