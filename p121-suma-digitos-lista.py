"""
• Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
• Se crea una función que suma los dígitos individuales de un número (ya la hicimos en clase)
• Se crea una función que recibe las lista capturada, usa la función anterior (suma dígitos) y recorre la lista
de números y suma sus dígitos, y regresa una lista con las sumas de tos dígitos de los números de la lista.
• Se imprime la lista original y la lista con las sumas de los dígitos de los números capturados.
Dame los números: 1971 2345 2015 2022
La lista de números original : [1971, 2345, 2015, 2022]
La lista con las suma de dígitos de los números: [18, 14, 8, 6]"""

def leer():
    lista=[]
    while True:
        n=float(input("numero: "))
        if n==-1:
            break
        lista.append(n)
    return lista

def sumadigitos(lista):
    lista2 = []
    for i in lista:
        suma = 0
        while i!=0:
            dig=i%10
            suma=suma+dig
            i=i//10
        lista2.append(suma)
    return lista2

lista = leer()
lista2 = sumadigitos(lista)
print("La lista original es: ", lista)
print("La suma de sus digitos es: ", lista2)
