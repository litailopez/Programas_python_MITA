"""Diseña un programa con una función que reciba tres parámetros: dos números (un rango), una letra P o I y nos
regrese la suma de números pares o impares en el rango de números especificados.
El programa deberá́ mostrar un menú́ con las opciones correspondientes y llamara a la función según la opción
seleccionada."""

import os

os.system('cls')

def impares_pares(inicio, final, PI):
    s=0
    if PI == "P":
        for par in range(inicio,final+1,2):
            print(par,end=' ')
            s = s + par        
    elif PI == "I":
        for impar in range(inicio,final+1,2):
            print(impar,end=' ')
            s=s+impar
    return s
# Programa principal
print("Dame el inicio, final y [I o P]: ")
a,b,c=int(input()),int(input()),str.upper(input())
print(" La suma es: ", impares_pares(a,b,c))




