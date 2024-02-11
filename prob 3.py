import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
       
        area = math.pi * (self.radio ** 2)
        return area


radio = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(radio)
area = circulo.calcular_area()
print("El área del círculo es:", area)