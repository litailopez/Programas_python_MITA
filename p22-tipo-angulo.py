# Calcular un ángulo en base a su magnitud
# <90 agudo, =90 recto, >90 y <180 obtuso, =180 llano, <180 y >360 concavo, =360 completo

import os ; os.system('cls')
angulo = int (input("Dame el angulo: "))

if angulo>=0 and angulo<=360:
    print("Continuamos...")
    if angulo < 90:
        print("Agudo")
    elif angulo == 90:
        print("Recto")
    elif angulo>90  and angulo < 180:
        print("Obtuso")
    elif angulo == 180:
        print("llano")
    elif angulo>180 and angulo<360:
        print("Concavo")
    else:
        print("Completo")
else:
    print("Angulo fuera de rango")