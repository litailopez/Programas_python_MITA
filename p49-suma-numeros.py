# imprime suma y promedio de n números introducidos por el usuario



c = int(input('Cuantos numeros ? '))
suma = 0
promedio = 0
for i in range(1,c+1):
    n = int(input(f"Número {i}? "))
    suma = suma + n
    promedio = suma / c
    
print(f'\nLa suma es {suma}')
print(f'\nEl promedio es {promedio:.2f}')
    