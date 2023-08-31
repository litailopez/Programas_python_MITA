# Calcular el volumen de un cilindro dado su radio y altura.

print("Calcular el volumen de un cilindro dado su radio y altura.\n")

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

volumen = 3.1416 * (radio ** 2) * altura

print(f"El volumen del cilindro es: {volumen:.2f} unidades cúbicas")

print("\nFin del programa")