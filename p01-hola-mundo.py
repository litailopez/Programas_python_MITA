#Lee datos del usuario y envia un saludo a la pantalla


print("Leyendo datos y enviando un mensaje a pantalla \n")

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
peso = float(input("Escribe tu peso: "))

print(f"\n Hola {nombre} tu edad es {edad} y tu peso es {peso} \n")

print(type(nombre))
print(type(edad))
print(type(peso))