
def contar_lineas_codigo(ruta_archivo):
    try:
        
        if not ruta_archivo.endswith(".py"):
            print("El archivo no tiene extensión .py. Ingrese un archivo válido.")
            return

        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()

           
            contador_lineas_codigo = 0
            for linea in lineas:
                if linea.strip() and not linea.strip().startswith("#"):
                    contador_lineas_codigo += 1

            print(f'Número de líneas de código en "{ruta_archivo}": {contador_lineas_codigo}')

    except FileNotFoundError:
        print(f'Archivo no encontrado. Verifique la ruta y el nombre del archivo.')

if __name__ == "__main__":
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)
