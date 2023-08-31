# Verificar si la suma de dos enteros es igual a un tercer entero

print("Verificar si la suma de dos enteros es igual a un tercer entero\n")
print("Ingrese tres números enteros:")

n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3:
    print("La suma de los dos primeros números es igual al tercer número")
else:
    print("La suma de los dos primeros números no es igual al tercer número")

print("\nFin del programa")
