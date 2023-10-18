"""• Dados los siguientes números:
◦ 50,60,70,80,90,100,200
◦ 60,90,100,300,400,500
◦ 10,20,60,90,70,100,600,700
• Crear tres conjuntos, uno por cada lista de números y mostrarlos ( A, B, C)
• Calcula y muestra:
◦ unión de los conjuntos A y B ( A | B )
◦ unión de los conjuntos B y C ( B | C )
◦ diferencia de A y C ( A - C)
◦ diferencia simétrica de B y C ( B ^ C)
◦ intersección de B y C ( B & C )
• Calcula y responda a las siguientes preguntas>
◦ A es subconjunto de B ?
◦ C es subconjunto de A ?
◦ 100 esta en A ?
◦ 60 esta en A , y en B y en C ?
◦ 900 no esta en C ?"""

import os
os.system('cls')

A = {50,60,70,80,90,100,200}
B = {60,90,100,300,400,500}
C = {10,20,60,90,70,100,600,700}


print("\nUnion: ")
print(f"A union B : {A | B}")
print(f"B union C : {B | C}")

print("\nDiferencia:")
print(f"A diferencia C: {A - C}")

print("\nDiferencia simetrica:")
print(f"B diferenia simetrica C: {B ^ C}")

print("\nIntersección: ")
print(f"B interseccion C: {B & C}")

print("\nSbconjuntos")
print(f"A es subconjunto de B ? : {A<=B} ")
print(f"C es subconjunto de A ? : {C<=A} ")

print(f"\n100 esta en A: {100 in A}")

print(f"\n60 esta en A, B, C: {60 in A & B & C}")

print(f"\n900 no esta en C: {900 not in C}")

