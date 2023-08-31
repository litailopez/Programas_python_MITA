# Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte.

print("Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte.\n")

numero = int(input("Ingrese su año de nacimiento: "))

d1 = numero // 1000
d2 = (numero - d1 * 1000) // 100
d3 = (numero - (d1 * 1000 + d2 * 100)) // 10
d4 = numero - (d1 * 1000 + d2 * 100 + d3 * 10)

print(f"Los digitos son {d1}, {d2}, {d3} y {d4}\n")
print(f"Su numero de la suerte es {d1 + d2 + d3 + d4}")

print("\nfin del programa")