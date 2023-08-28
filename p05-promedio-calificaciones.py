# Calcular el promedio de tres calificaciones 

print("Calcular el promedio de 3 calificaciones \n")

print("Ingrese las calificaciones separadas por un espacio entre ellas: ")
c1, c2, c3 = input().split()
c1, c2, c3 = float(c1), float(c2), float(c3)

suma = c1 + c2 + c3
promedio = suma / 3

print(f"Las calificaciones son: , {c1}, {c2}, {c3}, la suma es: {suma} ,  y el promedio es: {promedio:.2f}")