"""Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:
¿Cuántos términos?? 5
Salida: 1 + 1/2! + 1/3! + 1/4! + 1/5! , suma: 2.283333333333333"""

import os

os.system('cls')


n = int(input('Cuantos números ? '))
for i in range(1,n+1):
    f=1
    suma = 0
    for j in range(1,i+1):
        f = f * j
        suma = suma + (1/f)
    print(f" 1/{i}!", end="")
print( " = ", suma)



