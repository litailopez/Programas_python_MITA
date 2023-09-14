"""Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar el resultado e imprimir
un mensaje de acuerdo al promedio obtenido:
• >0 y <= 6 Quedas reprobado
• >6 a <=7 Pasas de panzazo
• >7 y <=8 Muy bien, pues mejorar
• >8 y <=9 Excelente sigue así
• >9 y <=10 Perfecto tu esfuerzo valió la pena
"""

print("Dame 5 calificaciones separadas por un enter: ")
n1, n2, n3, n4, n5 = float(input()), float(input()), float(input()), float(input()), float(input())

promedio = (n1 + n2 + n3 + n4 + n5)/5

print(f"Tu promedio es: {promedio}")

if promedio>0 and promedio<=6:
    print("Estas reprobado")
elif promedio>6 and promedio<=7:
    print("Apenas pasas")
elif promedio>7 and promedio<=8:
    print("Puedes mejorar")
elif promedio>8 and promedio<=9:
    print("Excelente, sigue asi")
else:
    print("Perfecto el esfuerzo valió la pena")
    