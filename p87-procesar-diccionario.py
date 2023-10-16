"""• Se tienen los datos de nombres y sueldos de los siguientes trabajadores, en dos listas:
Nombres: Juan, Pedro, Manuel, Elias, Maria, Felipe, Julia, Roberto
Sueldos: 4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00
• Crear un diccionario con ambas listas
• Mostrar el diccionario resultante
• Iterar por los elementos del diccionario:
o Usando las llaves : keys()
o Usando los valores: values()
o Usando la llave y el valor en base a la llave
o Usando el para llave/valor items()
• Obtener lo suma de los sueldos
• Obtener el promedio de los sueldos."""

trabajadores = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldo = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

dic = dict(zip(trabajadores, sueldo))

for k in dic.keys():
    print(k, end=', ')

print('\n')
for v in dic.values():
    print(v, end=', ')

print('\n')
s=p=0
for n,e in dic.items():
    print(f'{n:<10} - {e:3}')
    s= s + e
    p = s /len(dic)
        
print(f'\n\nLa suma: {s} y el promedio es: {s/len(dic)}')