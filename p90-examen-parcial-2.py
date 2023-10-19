import os
os.system('cls')

# Diccionario con los precios de los ingredientes
precios_ingredientes = {
    'T': 1.50,
    'P': 3.50,
    'A': 0.40,
    'Q': 3.74,
    'I': 2.10
}

# Precio base de la pizza
precio_base = 15.00

# Función para calcular el precio del pedido
def calcular_precio_pedido(pedido):
    total = precio_base
    for ingrediente in pedido:
        if ingrediente in precios_ingredientes:
            total += precios_ingredientes[ingrediente]
        else:
            return None  # Ingrediente inválido, se retorna None
    if total > 30:
        subtotal = total
        total *= 0.95  # Aplicar 5% de descuento si el total excede los 30
        if subtotal != total:
            print(f"subtotal: {subtotal:.2f}")
    return total

# Función para mostrar los posibles ingredientes
def mostrar_ingredientes_disponibles():
    print("Ingredientes disponibles:")
    print("Precio base es de 15, compra de más de 20 descuento del 5%")
    for ingrediente, precio in precios_ingredientes.items():
        print(f"{ingrediente} - {precio}")

# Programa principal
pedido = input("Ingrese los ingredientes de su pizza (por ejemplo, TT, TPQI): ").upper()


if not pedido:
    mostrar_ingredientes_disponibles()
else:
    total_pedido = calcular_precio_pedido(pedido)
    if total_pedido is not None:
        print("Ingredientes de tu pizza:", pedido)
        print(f"Total a pagar: ${total_pedido:.2f}")
    else:
        print("Error: Alguno de los ingredientes ingresados es inválido.") 