# Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, si no lo son(1,4,6) mandar mensaje de error.

print("Dame tres numeros enteros separados por un enter: ")
n1, n2, n3 = int(input()), int(input()), int(input()) 

if (n2 == n1 + 1) and (n3 == n2 +1):
    print("Los numeros son consecutivos")

else:
    print("Numeros no consecutivos") 