# Uso de las funciones trigonométricas en python

import math

print("Calculo de las funciones trigonometricas basicas\n")
angulo = float(input("Ingrese el valor del angulo en grados: "))
radianes = math.radians(angulo)

sen = math.sin(radianes)
cos = math.cos(radianes)
tan = math.tan(radianes)

#print (f"Seno: {sen} \nCoseno: {cos} \nTangente: {tan}")

salida = ("Resumen de funciones trigonometricas\n"
          f'El seno es {sen} \n'
          f'El coseno es {cos} \n'
          f'La tangente es {tan} \n'
          f'El angulo es de {angulo} grados y equivale a {radianes} radianes\n'
          )

print(salida)