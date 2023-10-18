"""Dados los siguientes nombres:
• Juan, Maria, Pedro, Jose, Rocio
• Pedro, Juan, Pablo, Mateo, Esther
• Crea dos conjuntos uno para cada lista de nombres y muéstralos ( A, B )
• Calcula y muestra:
◦ union de los conjuntos ( A | B)
◦ intesección de los conjuntos ( A & B)
◦ diferenia de los conjuntos ( A - B )
◦ diferencia simetrica de los conjuntos ( A ^ B )
• Calcula y muestra también
◦ si el conjunto de nombres Pablo, Mateo, es subconjunto de B
◦ si el conjunto A, es superconjunto del conjunto de nombres: Reynaldo, Angelica
◦ si Pedro esta en A
◦ si Lilia no esta en B"""

import os
os.system('cls')

A = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
B = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}
C = {'Pablo', 'Mateo'}
D = {'Reynaldo', 'Angelica'}

print("\nUnion: ")
print(f"A union B : {A | B}")

print("\nIntersección: ")
print(f"A interseccion B: {A & B}")

print("\nDiferencia:")
print(f"A diferencia B: {A - B}")

print("\nDiferencia simetrica:")
print(f"A diferenia simetrica B: {A ^ B}")

print(f"\nsi el conjunto de nombres Pablo, Mateo, es subconjunto de B {C<=B} ")

print(f"\nsi el conjunto A, es superconjunto del conjunto de nombres Reynaldo, Angelica : {A>=D}")

print(f"\nsi Pedro esta en A : {'Pedro' in A}")

print(f"\nsi Lilia no esta en B : {'Lilia' not in B}")




