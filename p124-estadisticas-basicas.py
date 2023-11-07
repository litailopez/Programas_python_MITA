"""
Dame números: 5 6 6 7 8 9 10 10
Lista de números: [5, 6, 6, 7, 8, 9, 10, 10]
La media: 7.625
Mayor de los datos: 10
Menor de los datos: 5
Varianza: 3.234
Desviación estándar: 1.798"""

import math

def leer():
    arreglo=[]
    while True:
        n=int(input("numero: "))
        if n==-1:
            break
        arreglo.append(n)
    return arreglo

# Función para encontrar el valor máximo en el arreglo
def encontrar_maximo(arreglo):
    if len(arreglo) == 0:
        return None
    maximo = arreglo[0]
    for num in arreglo:
        if num > maximo:
            maximo = num
    return maximo

# Función para encontrar el valor mínimo en el arreglo
def encontrar_minimo(arreglo):
    if len(arreglo) == 0:
        return None
    minimo = arreglo[0]
    for num in arreglo:
        if num < minimo:
            minimo = num
    return minimo

# Función para calcular la media (promedio) de los elementos en el arreglo
def calcular_media(arreglo):
    if len(arreglo) == 0:
        return None
    suma = sum(arreglo)
    media = suma / len(arreglo)
    return media

# Función para calcular la varianza poblacional
def calcular_varianza(arreglo):
    if len(arreglo) == 0:
        return None
    media = calcular_media(arreglo)
    suma_de_cuadrados = sum((x - media) ** 2 for x in arreglo)
    varianza = suma_de_cuadrados / len(arreglo)
    return varianza

# Función para calcular la desviación estándar poblacional
def calcular_desviacion_estandar(arreglo):
    if len(arreglo) == 0:
        return None
    varianza = calcular_varianza(arreglo)
    desviacion_estandar = math.sqrt(varianza)
    return desviacion_estandar

arreglo = leer()
print("La lista original es: ", arreglo)
print("Valor máximo:", encontrar_maximo(arreglo))
print("Valor mínimo:", encontrar_minimo(arreglo))
print("Media:", calcular_media(arreglo))
print("Varianza :", calcular_varianza(arreglo))
print("Desviación estándar :", calcular_desviacion_estandar(arreglo))