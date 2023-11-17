import os

class Jugador:
    def __init__(self, nombre, anio_nac, sexo, becado):
        self.nombre = nombre
        self.anio_nac = anio_nac
        self.sexo = sexo
        self.becado = becado

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def calcular_subtotal(self):
        subtotal = sum([jugador.becado == "Sin Beca" for jugador in self.jugadores]) * self.costo
        return subtotal

class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def calcular_total_categorias(self):
        return len(self.categorias)

    def calcular_total_hombres_mujeres(self):
        total_hombres = sum([sum([1 for jugador in categoria.jugadores if jugador.sexo == "Hombre"]) for categoria in self.categorias])
        total_mujeres = sum([sum([1 for jugador in categoria.jugadores if jugador.sexo == "Mujer"]) for categoria in self.categorias])
        return total_hombres, total_mujeres

    def imprimir_reporte(self):
        print("REPORTE DEL CLUB DEPORTIVO")
        print(f"Nombre: {self.nombre}")
        print(f"Propietario: {self.propietario}")
        print(f"Domicilio: {self.domicilio}")
        print(f"Total de Categorias: {self.calcular_total_categorias()}")
        total_hombres, total_mujeres = self.calcular_total_hombres_mujeres()
        print(f"Total de Hombres: {total_hombres}")
        print(f"Total de Mujeres: {total_mujeres}")
        print(">> Datos generales de las Categorias")

        for categoria in self.categorias:
            print(f"Nombre: {categoria.nombre} Rango: {categoria.rango} Costo: ${categoria.costo:.2f}")
            print(">> Jugadores por Categoria:")
            print(f"> {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})")

            for jugador in categoria.jugadores:
                print(f"Nombre: {jugador.nombre} AñoNac: {jugador.anio_nac} Sexo: {jugador.sexo} Becado: {jugador.becado}")

            subtotal = categoria.calcular_subtotal()
            print(f"- SubTotal : ${subtotal:.2f}\n")

        total_ingresos = sum([categoria.calcular_subtotal() for categoria in self.categorias])
        print(f"-> Total : ${total_ingresos:.2f}")

# Programa principal
os.system('cls')
jugador1 = Jugador("Alexander Lopez", 2006, "Hombre", "Sin Beca")
jugador2 = Jugador("Uriel Puga", 2007, "Hombre", "Becado")
jugador3 = Jugador("Alejandra Escalona", 2008, "Mujer", "Sin Beca")

jugador4 = Jugador("Armando Santana", 2009, "Hombre", "Sin Beca")
jugador5 = Jugador("Daniel Mijares", 2010, "Hombre", "Sin Beca")
jugador6 = Jugador("Antonio Hernandez", 2011, "Mujer", "Becado")

jugador7 = Jugador("Andrea Solis", 2012, "Mujer", "Becado")
jugador8 = Jugador("Marissa Hernandez", 2013, "Mujer", "Becado")
jugador9 = Jugador("Diana Soto", 2014, "Mujer", "Sin Beca")

categoria1 = Categoria("Junior A", "2006/2007/2008", 1250.00)
categoria1.agregar_jugador(jugador1)
categoria1.agregar_jugador(jugador2)
categoria1.agregar_jugador(jugador3)

categoria2 = Categoria("Junior B", "2009/2010/2011", 850.00)
categoria2.agregar_jugador(jugador4)
categoria2.agregar_jugador(jugador5)
categoria2.agregar_jugador(jugador6)

categoria3 = Categoria("Pony A", "2012/2013/2014", 700.00)
categoria3.agregar_jugador(jugador7)
categoria3.agregar_jugador(jugador8)
categoria3.agregar_jugador(jugador9)

academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")
academia.agregar_categoria(categoria1)
academia.agregar_categoria(categoria2)
academia.agregar_categoria(categoria3)

academia.imprimir_reporte()