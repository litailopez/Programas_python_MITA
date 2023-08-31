# Dados dos ángulos de un triángulo, calcular el 3er ángulo

print("Dados dos ángulos de un triángulo, calcular el 3er ángulo\n")

print("Ingrese los dos ángulos del triángulo:")
a1, a2 = float(input()), float(input())

a3 = 180 - (a1 + a2)

print(f"El tercer ángulo equivale a: {a3} grados")

print("\nFin del programa")