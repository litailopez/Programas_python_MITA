# Examen parcial 1
"""Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: Tipo
de usuario, paquete y cantidad.
• Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500
• Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900
Se debe calcular un subtotal de la venta sumando el precio del tipo de usuario más el precio de tipo de paquete,
y multiplicando por la cantidad solicitada.
Se otrgará un descuento siempre y cuando el subtotal sea mayor a 5,000 y de acuerdo a lo siguiente
• Es Alumno 20%
• Es Trabajador y un 10%
• Es Docente y un 5%"""


final_total = 0

while(True):


    precios_usuario = {1: 100, 2: 200, 3: 500}
    precios_paquete = {1: 600, 2: 800, 3: 900}
    usuario = {1: "Alumno", 2: "Trabajador", 3: "Docente"}
    paquete = {1: "Solo conferencias", 2: "Con eventos sociales", 3: "Con kit de acceso"}
    subtotal = 0
    total = 0
    descuento = 0

    print("Universidad Patio SA de CV")
    print("Sistema de Inscripción Congreso de Sistemas\n")
    tipo_usuario = int(input("Ingresa el tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500: "))
    tipo_paquete = int(input("Ingresa tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900: " ))
    cantidad = int(input("Ingresa la cantidad de inscripciones: "))

    subtotal = (precios_usuario[tipo_usuario] + precios_paquete[tipo_paquete])*cantidad


    if subtotal > 5000:
        if tipo_usuario == 1:
            descuento = subtotal*.20
            n_descuento = "(20.0%)"
        elif tipo_usuario == 2:
            descuento = subtotal*.10
            n_descuento = "(10.0%)"
        elif tipo_usuario == 3:
            descuento = subtotal*.05
            n_descuento = "(5.0%)"

    total = subtotal - descuento
    final_total = final_total + total 

    print(f"Tu pedido fue: {cantidad}, Tipo de usuario:  {usuario[tipo_usuario]}, Tipo de paquete: {paquete[tipo_paquete]}")
    print (f"Subtotal: ${subtotal} con un descuento de: ${descuento} {n_descuento} y un total de: ${total}")
    
    res = input("\nDeseas continuar (S/N)?: ").upper()
    if res == "N": break

print(f"Importe total de la venta: ${final_total} ")

print("\nProceso terminado")

