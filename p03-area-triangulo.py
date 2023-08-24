# Calcula el area de un Triángulo dada la base y altura.

import math # Importa el modulo de funciones y constantes matematicas.

print("Calculando el area de un triangulo \n")

print("Escribe la base y altura del triangulo separados por un enter: ")
base, altura = int(input("Base: ")), int(input("Altura: "))

area = (base * altura) / 2

print(f"Para un triangulo de base {base} y altura {altura} el area resultante es {area:.2f}")

