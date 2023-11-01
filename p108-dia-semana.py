# Diseña un programa con una función que pida un número entero entre 1 y 7 y devuelva el día de la semana con letra.

def dia(n):
    d=""
    if n==1:
        d="L"
    elif n==2:
        d="M"
    elif n==3:
        d="M"
    elif n==4:
        d="J"
    elif n==5:
        d="V"
    elif n==6:
        d="S"
    elif n==7:
        d="D"
    else:
        d="Error"
    return d

#Programa principal
n=int(input("Dame el dia de la semana (1-7): "))
print(f"El dia es {dia(n)}")