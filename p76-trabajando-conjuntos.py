import os 
os.system('cls')
municipios = {'Zacatecas', 'Guadalupe','Jerez','Fresnillo'}

print(f'\nLa colección es del tipo : {type(municipios)}')
print(f'Longitud del conjunto : {len(municipios)}')
print(f'El conjunto original : \n{municipios}\n')
print("\nLista de municipios usando un ciclo: ")
for mun in municipios:
    print(mun,end=' ')
    
print('\nAgregra elementos a un conjunto:\n')
municipios.add("Teul")
print(f'Agregar con Add() a Teul : \n{municipios}\n')

otrosmunicipios = {"Luis Moya","Ojocaliente","Tepetongo"}
municipios.update(otrosmunicipios)
print(f'Agregrar con Update() Luis Moya, Ojocaliente, Tepetongo: \n{municipios}\n')

print("\nEliminar elementos del conjunto:\n")
municipios.remove('Zacatecas')
print(f'Eliminar con Remove() a Zacatecas: \n{municipios}\n')

municipios.discard("Ojocaliente")
print(f'Eliminar con Discard() Ojocaliene: \n{municipios}\n')

mun=municipios.pop()
print(f'Eliminar con Pop() (al primero): \n{municipios} \n{mun}\n')

municipios.clear()
print(f'Eliminar con Clear() : \n{municipios}\n')