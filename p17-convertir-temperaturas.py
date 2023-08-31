# Convierte grados Celsius a Fahrenheit y viceversa

print("Convierte grados Celsius a Fahrenheit y viceversa\n")
opcion = str.upper(input("Ingrese [C] para convertir de Celsius a Fahrenheit\n [F] para convertir de Fahrenheit a Celsius\n Elije: "))

if opcion == 'C':
    print("Convierte de Celsius a Fahrenheit")
    temp = float(input("Ingrese la temperatura en grados Celsius: "))
    res = (temp * 9/5) + 32
    print(f"{temp} grados Celsius son {res:.2f} grados Fahrenheit")

else: 
    print("Convierte de Fahrenheit a Celsius")
    temp = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    res = (temp - 32) * 5/9
    print(f"{temp} grados Fahrenheit son {res:.2f} grados Celsius")

print("Fin del programa")    