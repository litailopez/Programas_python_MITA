# Aceptar estudiantes en base a su edad y calificaciones

nombre = input("Dame tu nombre: ")
edad = int(input ("Dame tu edad: "))

if edad >= 18:
    print("Continuamos..")
    print("Dame dos calificaciones separadas por un enter: ")
    c1, c2 = int(input()), int(input())
    if c1>=8 and c2>=8:
        print(f"{nombre} bienbenid@ tus calificaciones son {c1} y {c2}")
    else:
        print("Solo aceptamos calificaciones mayores a 8")
    
else:
    print("Solo aceptamos mayores de edad")