"""Diseña un programa con dos funciones que convierta: pulgadas a centímetros y metros a pies. Deberá́ mostrar un
menú con las opciones correspondientes.
Considere las siguientes formulas:
 centímetros = pulgadas * 2.54
 pies = metros * 3.281"""

def pulgadas(med):
    return(med*2.54)

def pies(med):
    return(med*3.281)

#Programa principal
print("[ P ] Pulgadas a centimetros")
print("[ M ] Metros a pies")

op=input("Elije: ").upper()


if op=="P":
    med=int(input("Dame pulgadas: "))
    print(f"los centimetros {pulgadas(med)}")
elif op=="M":
    med=int(input("Dame metros: "))
    print(f"los pies {pies(med)}")
else:
    print("Opcion incorrecta")
