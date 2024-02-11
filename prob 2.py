def obtener_calificaciones():
    while True:
        try:
          
            entrada = input("Ingrese las calificaciones separadas por comas: ")
            
         
            calificaciones_str = entrada.split(',')
            
        
            calificaciones = [int(cal) for cal in calificaciones_str]
            
            print("Calificaciones:", calificaciones)
            break
        except ValueError:
            print("Error: Asegúrese de ingresar valores numéricos válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    obtener_calificaciones()