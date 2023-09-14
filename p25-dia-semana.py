""" Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo,
2 es lunes y así hasta 7 es sabado. Si el número no está en el rango especificado, mostrar un mensaje de error."""

dia = int(input("Elije un número del 1 al 7: "))

if dia == 1:
    print("Tu dia es Domingo")
elif dia == 2:
    print("Tu dia es Lunes")
elif dia == 3:
    print("Tu dia es Martes")
elif dia == 4:
    print("Tu dia es Miercoles")
elif dia == 5:
    print("Tu dia es Jueves")
elif dia == 6:
    print("Tu dia es Viernes")
elif dia == 7:
    print("Tu dia es Sabado")
else:
    print("El numero no se encuentra en el rango de dias")