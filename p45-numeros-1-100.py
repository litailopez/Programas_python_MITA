# Imprime los números de 1 a n
# for n in range (inicio, final, cuánto)

x = int(input("Hasta dónde?: "))
y = int(input("De cuánto en cuánto?"))

for i in range(1, x+1, y):
    print(i, end=" ")