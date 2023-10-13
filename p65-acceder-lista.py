"""Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988.
Después, acceda y muestre:
• El primero elemento
• El último elemento
• El elemento : 999
• Los elementos entre: 123 a 999
• Los elementos desde el inicio hasta el 222
• Los elementos desde 222 hasta el final
• Los tres úlitmos elementos usando índice negativo"""

import os

os.system('cls')
#         0   1     2   3     4   5    6    7    8    9 
nums = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
#        -10  -9  -8    -7  -6    -5  -4    -3   -2  -1    

print(f'Primer elemento : {nums[0]} \n')
print(f'último elemento : {nums[-1]} \n')
print(f'Elemento 999 : {nums[4]} \n')
print(f'Elementos 123 a 999 : {nums[1:5]} \n')
print(f'Elementos desde inicio hasta 222 : {nums[:4]} \n')
print(f'Elementos desde 222 hasta el final : {nums[3:]} \n')
print(f'Tres ultimos elementos: {nums[-3:]}')