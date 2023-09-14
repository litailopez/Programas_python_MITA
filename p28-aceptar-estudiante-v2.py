""" Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. La
Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5.
"""

Nombre = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu sexo [H] hombre [M] mujer: ").upper()
edad = int(input("Ingresa tu edad: "))
print("Dame tres calificaciones separadas por un enter: ")
n1, n2, n3 = float(input()), float(input()), float(input())

promedio = (n1 + n2 + n3)/3
print(f"Estudiante {Nombre}, de sexo {sexo}, con edad de {edad} y promedio de {promedio:.2f}")

if sexo == "M" and edad>21 and promedio>8 and promedio<=9.5:
    print("Fuiste aceptado")
else:
    print("No cumples con los requisitos, no eres aceptado")
