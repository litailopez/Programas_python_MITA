
# Calcular la hipotenusa de un triángulo rectángulo conocidas las longitudes de sus dos catetos.
 
import math

print("Ingrese la longitud de los catetos separados por un espacio entre ellos: ")
c1, c2 = input().split()
c1, c2 = float(c1), float(c2)

hipotenusa = math.sqrt(c1*c1 + c2*c2)

print(f"La hipotenusa es: {hipotenusa:.2f}")

