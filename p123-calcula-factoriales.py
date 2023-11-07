"""
• Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
• Se crea una función que calcula el factorial de un número (ya la hicimos en clase)
• Se crea una función que recibe las lista capturada, usa la función anterior (calcular factorial) que recorre la
lista de números y calcula el factorial de cada uno de ellos, y regresa como resultado una lista con los
factoriales de los números de la lista.
• Se imprime la lista original y la lista con los factoriales de los números capturados.
Dame los números: 2 5 8 9
La lista de números originales: [2, 5, 8, 9]
La lista con los factoriales: [2, 120, 40320, 362880]"""

def leer():
    lista=[]
    while True:
        n=int(input("numero: "))
        if n==-1:
            break
        lista.append(n)
    return lista

def factorial(lista):
    factoriales = []
    for i in lista:
        f=1
        for i in range(1,i+1):
            f=f*i
        factoriales.append(f)    
    return factoriales

lista = leer()
lista2 = factorial(lista)
print("La lista original es: ", lista)
print("Los factoriales son: ", lista2)
   
    