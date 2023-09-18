# Calcula e imprime los números de la conjetura de collatz
import os


while(True):
    os.system('cls')
    num = int(input("Dame un numero entero positivo: "))

    while(num != 1):
        print(num, end = ' ')
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1

    print (num, end =' ')
    res = input("Deseas continuar (S/N)?: ").upper()
    if res == "N": break

print("\nProceso terminado")