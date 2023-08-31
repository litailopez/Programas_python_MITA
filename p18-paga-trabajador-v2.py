# Calcula la paga de un trabajador considerando que las horas extras se pagan al doble de una hora normal

print("Calcula la paga de un trabajador considerando que las horas extras se pagan al doble de una hora normal\n")

nombre = input("Ingrese el nombre del trabajador: ")
horas = int(input("Ingrese las horas trabajadas: "))
pago = float(input("Ingrese el pago por hora: "))

extra = 0

if horas > 40:
    extra = horas - 40
    total = (40 * pago) + (extra * pago * 2)
else:
    total = horas * pago

print(f"El trabajador {nombre} trabajó {horas} horas con paga de {pago}, horas extra {extra}, su paga total es de ${total:.2f}")