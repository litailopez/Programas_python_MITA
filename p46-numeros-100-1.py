# Imprime los números de 100 a n
# for n in range (inicio, final, cuánto)

x = int(input("Desde dónde?: "))
y = int(input("De cuánto en cuánto?"))

for i in range(100, 0, -y):
    print(i, end=" ")