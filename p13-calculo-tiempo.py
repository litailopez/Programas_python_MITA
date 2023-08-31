# Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos.

print("Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos. \n")

horas = int(input("Ingrese la cantidad de horas: "))
dias = horas / 24
minutos = horas * 60
segundos = horas * 3600

print(f"La cantidad de horas ingresadas es: {horas} horas y equivale a {dias} días, {minutos} minutos y {segundos} segundos.")

print("\nFin del programa.")