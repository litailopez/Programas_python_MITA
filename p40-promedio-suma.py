"""Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0,
además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse hasta que el usuario lo
decida."""

import os

while(True):

    cuenta = suma = prom = 0 
    os.system('cls')

    while(True):
        num = int(input("Numero? "))
        if num != 0:
            cuenta = cuenta + 1
            suma = suma + num
            prom = suma / cuenta

        else:
            break

    print(f"Se introdujeron {cuenta} numeros")
    print(f"La suma de los numeros es {suma}")
    print(f"El promedio es {prom:.2f}")
    
    res = input("\nDeseas continuar (S/N)?: ").upper()
    if res == "N": break

print("\nProceso terminado")
