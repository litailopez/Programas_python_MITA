# Agregar elementos a la lista

import os 
os.system('cls')

#       1     2     3     4 
nums = [80.3, 12.5, 60.2, 30.4]

print(f'Longitud de lista : {len(nums)} \n')
print(f'todos los números : {nums}\n')
nums.append(90)
nums.append(100)
print(f'Longitud de lista : {len(nums)} \n')
print(f'agregar al final : {nums}\n')
nums.insert(4,80)
print(f'Longitud de lista : {len(nums)} \n')
print(f'insertar : {nums}\n')
otros = [110,120,130]
nums.extend(otros)
print(f'Longitud de lista : {len(nums)} \n')
print(f'extender con : {nums}\n')