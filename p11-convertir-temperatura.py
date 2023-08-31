# Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit.

print("Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit.\n")

grados = float(input("Ingrese la temperatura en grados celcius: "))
temp = (grados * 9/5) + 32
print(f"La temperatura en grados farenheit es: {temp:.2f} grados")

print("\nFin del programa")