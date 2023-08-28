# Dividir un número entero de tres cifras  en centenas, decenas y unidades

print("Dividir un número entero de tres cifras  en centenas, decenas y unidades\n")

numero = int(input("Ingrese un número entero de tres cifras: "))
centenas = numero // 100
decenas = (numero - centenas * 100) // 10
unidades = numero - (centenas * 100 + decenas * 10)

print(f"El número {numero} tiene {centenas} centenas, {decenas} decenas y {unidades} unidades")
print (f"Suma de cifras: {centenas} + {decenas} + {unidades} = {centenas + decenas + unidades}")