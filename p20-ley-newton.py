# Calcula la segunda ley de Newton (f = m * a)

print("[F]uerza     (f = m * a)")
print("[M]asa       (m = f / a)")
print("[A]celeracion (a = f / m)")

op = input ("Elige: ").upper()

if op == "F":
    print("Calculando fuerza")
    m = float(input("Dame la masa: "))
    a = float(input("Dame la aceleracion: "))
    f = m*a
    print(f"\nLa fuerza es {f:.2f}")
elif op == "M":
    print("Calculando masa")
    f = float(input("Dame la fuerza: "))
    a = float(input("Dame la aceleracion: "))
    m = f/a 
    print(f"\nLa masa es {m:.2f}")
elif op == "A":
    print("Calculando aceleracion")
    f = float(input("Dame la fuerza: "))
    m = float(input("Dame la masa: "))
    a = f/m 
    print(f"\nLa masa es {a:.2f}")
else:
    print("\n Opcion inválida")