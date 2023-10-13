"""Crear un programa que permita procesar una lista de n números enteros, de acuerdo a lo siguiente:
• Leer n números por parte del usuario
• Agregar cada número a la lista
• Mostrar la lista
• Iterar por la lista y sacar la suma de sus elementos
• Calcular luego el promedio de los n"""

import os

os.system('cls')

n = int(input("Ingrese la cantidad de números: "))

suma = 0
numeros = []

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i + 1)))
    numeros.append(numero)


print("Lista de números ingresados:", numeros)


suma = sum(numeros)


promedio = suma / n

print("Suma de los números:", suma)
print("Promedio de los números:", promedio)