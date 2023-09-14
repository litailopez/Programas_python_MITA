# Dados tres números enteros, verificar cual es el mayor.

print("Dame tres numeros enteros separados por un enter: ")
n1, n2, n3 = int(input()), int(input()), int(input())

if n1 > n2 and n1 > n3:
    print(f"El numero mayos es {n1}") 
elif n2 > n1 and n2 > n3:
    print(f"El numero mayos es {n2}")
elif n3 > n1 and n3 > n2:
    print(f"El numero mayos es {n3}")
else:
    print("Exiten números mayores iguales")  