# Calcula el area de un circulo dado el radio.

import math # Importa el modulo de funciones y constantes matematicas.

print("Calculando el area de un circulo \n")

radio = float(input("Escribe el radio del circulo: "))

area = math.pi * radio**2 # Calcula el area del circulo.

print(f"Para un circulo de radio {radio} el area resultante es {area:.2f}")