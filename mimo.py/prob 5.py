class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None
    
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad}")
        print(f"Notas: {self.notas}")
    
    def set_age(self, edad):
        
        self.edad = edad
    
    def set_notas(self, notas):
       
        self.notas = notas


nombre_alumno = input("Ingrese el nombre del alumno: ")
numero_registro_alumno = input("Ingrese el número de registro del alumno: ")

alumno = Alumno(nombre_alumno, numero_registro_alumno)


edad_alumno = int(input("Ingrese la edad del alumno: "))
alumno.set_age(edad_alumno)

notas_alumno = input("Ingrese las notas del alumno (separadas por comas): ").split(',')
notas_alumno = [float(nota) for nota in notas_alumno]
alumno.set_notas(notas_alumno)

alumno.display()