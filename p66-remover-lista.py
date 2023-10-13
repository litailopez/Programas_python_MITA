"""Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988.
Después remover elementos como sigue:
• Remover con de los elementos 100, 123, 456
• Remover con remove() los elementos 322, 988
• Remover con pop() el elemento 222 y mostrarlo
• Remover con pop() el último elemento hasta ahora y mostrarlo
• Mostrar la lista resultante para comprobar

Considere que la lista va ir perdiendo elementos, para que considere las posiciones a utilizar en los comandos
anteriores.
La lista resultante: 999, 895, 325
• Remover con clear() todos los elementos, resultando una lista vacia."""

import os 
os.system('cls')
#        0    1    2    3    4    5    6    7    8    9         
nums = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]

nums.remove(100)
nums.remove(123)
nums.remove(456)
nums.remove(322)
nums.remove(988)
# [222, 999, 895, 325, 234]
num = nums.pop(0)
print(f'Numero removido -> {num}')
num2 = nums.pop()
print(f'Numero removido -> {num2}')
print(f'Lista nueva: {nums}')
nums.clear()
print(f'remover todos : {nums}\n')