# Se desea imprimir los números de 1 a n de 10 en 10

import os

os.system('cls')

x = int(input("Hasta dónde?: "))

for i in range(1, x+1, 10):
    print(i, end=" ")