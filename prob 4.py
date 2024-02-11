class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        
        area = self.largo * self.ancho
        return area

largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
rectangulo = Rectangulo(largo, ancho)
area = rectangulo.calcular_area()
print("El área del rectángulo es:", area)