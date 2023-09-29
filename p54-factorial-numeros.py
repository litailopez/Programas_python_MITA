# Imprime el factorial de n números
import os

os.system('cls')


n = int(input('Cuantos números ? '))
for i in range(1,n+1):
    print(f"{i}! -> ", end="")
    f=1
    for j in range(1,i+1):
        print(f"{j} * ", end="")
        f = f * j
    print(f" = {f}")