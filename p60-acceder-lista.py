# Acceder a los elementos de una lista

import os


os.system('cls')
#       0   1   2   3   4   5   6   7   8
nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]
#       -9  -8  -7  -6  -5  -4  -3  -2  -1    

print(f'Longitud de lista : {len(nums)} \n')
print(f'Todos los números : {nums} \n')
print(f'Primero y último : {nums[0]}, {nums[-1]} \n')
print(f'Del 2 al 6 : {nums[2:6]} \n')
print(f'Los primeros 3 : {nums[:3]} \n')
print(f'Los últimos 3 : {nums[6:]} \n')