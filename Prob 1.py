def calcular_porcentaje(x, y):
    try:
      
        x = int(x)
        y = int(y)
        if x <= y and y != 0:
       
            porcentaje = round((x / y) * 100)
            
            
            if porcentaje < 1:
                return 'E'
            elif porcentaje > 99:
                return 'F'
            else:
                return f'{porcentaje}%'
        else:
            raise ValueError("X debe ser menor o igual a Y, y Y no puede ser 0.")
    except ValueError:
        return "Error: X y Y deben ser números enteros."
    except ZeroDivisionError:
        return "Error: Y no puede ser 0."

def main():
    while True:
       
        entrada = input("Ingrese una fracción en formato X/Y: ")
        
      
        partes = entrada.split('/')
        
    
        if len(partes) == 2:
            resultado = calcular_porcentaje(partes[0], partes[1])
            print(f"Resultado: {resultado}")
            break
        else:
            print("Formato incorrecto. Ingrese la fracción en formato X/Y.")

if __name__ == "__main__":
    main()