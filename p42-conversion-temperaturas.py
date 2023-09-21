"""Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores
introducidos por el usuario, es decir el usuario introduce la temperatura inicial y la temperatura final en grados
centígrados y el programa realiza la conversión a farenheit incrementando el valor inicial en 1, hasta llegar al valor
final. El proceso debe poder repetirse hasta que el usuario lo decida."""

import os

while(True):
    os.system('cls')
    while (True):
        ti = float(input("Temperatura inicial: "))
        tf = float(input("Temperatura final: "))
        if (ti < tf ): break

    c = ti
    print("°C\t°F")
    print("_"*15)
    while (c <= tf):    
        print(f'{c}\t{c*(9/5)+32:.2f}')
        c = c + 1
    print("_"*15)
    res = input("Deseas continuar (S/N)?: ").upper()
    if res == "N": break

print("\nProceso terminado")