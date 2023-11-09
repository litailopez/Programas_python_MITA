import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def obtenerArea(self):
        return math.pi * math.pow(self.radio,2)
    def circunferencia(self):
        return 2 * math.pi * self.radio
    def __str__(self):
        return f"Circulo [Radio = {self.radio:.2f}]"

# Programa princial
circulo1 = Circulo(10.40)
print(f'\nPrimer Circulo {circulo1}')
print(f'Area : {circulo1.obtenerArea():.2f}')
print(f'Circunferencia : {circulo1.circunferencia():.2f}')
print(f'\nPrimer Circulo {circulo1}')
circulo2 = Circulo(12.45)
print(circulo2)
print(f'Area : {circulo2.obtenerArea():.2f}')
print(f'Circunferencia : {circulo2.circunferencia():.2f}')