# Calcula la paga de un trabajador 

print("Calculando la paga de un trabajador \n")

nombre = input("Escribe tu nombre: ")
horas = int(input("Escribe tus horas trabajadas: "))
paga = float(input("Escribe tu paga por hora: "))

tasa = 0.03

paga_bruta = horas * paga
impuestos = paga_bruta * tasa
paga_neta = paga_bruta - impuestos

print("\n Resumen de pagos \n")
print(f"{nombre} trabajo {horas} horas con una paga de {paga} pesos a una tasa de {tasa} \n")
print(f"La paga bruta es de {paga_bruta} pesos")
print(f"Los impuestos son de {impuestos} pesos")
print(f"La paga neta es de {paga_neta} pesos")