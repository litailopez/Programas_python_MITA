# Cambiar los elementos de una lista 

import os
os.system('cls')

#       1   2  3    4    5    6  7  8    9        
nums = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print(f'Longitud de lista : {len(nums)} \n')
print(f'todos los números : {nums}\n')
print(f"Tipo :  {type(nums)}")
nums[0] = 7
nums[1] = 7
print(f'modificar 0 y 1 : {nums}\n')
nums[2:5] = [9,9,9]
print(f'modificar 2:5 - : {nums}\n')
nums[-1] = 6.0
print(nums,"\n")
nums[6] = nums[6] + 5.0
print(nums,"\n")