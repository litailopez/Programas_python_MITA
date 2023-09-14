"""Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V,
VI, VII, VIII, IX, X). Si el número no esta en el rango solicitado que mande un mensaje de error."""

dia = int(input("Elije un número del 1 al 10: "))

if dia == 1:
    print("El numero romano es I")
elif dia == 2:
    print("El numero romano es II")
elif dia == 3:
    print("El numero romano es II")
elif dia == 4:
    print("El numero romano es IV")
elif dia == 5:
    print("El numero romano es V")
elif dia == 6:
    print("El numero romano es VI")
elif dia == 7:
    print("El numero romano es VII")
elif dia == 8:
    print("El numero romano es VIII")
elif dia == 9:
    print("El numero romano es IX")
elif dia == 10:
    print("El numero romano es X")
else:
    print("El numero no se encuentra en el rango")