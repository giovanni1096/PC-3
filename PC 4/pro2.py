
from pyfiglet import Figlet

import random

def imprimir_con_fuente():
    f = Figlet()
    fuentes_disponibles = f.getFonts()

    fuente_seleccionada = input("Ingrese el nombre de la fuente (o presione Enter para seleccionar aleatoriamente): ")
    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes_disponibles)

    texto_imprimir = input("Ingrese el texto que desea imprimir: ")

    try:
    
        f.setFont(font=fuente_seleccionada)

        print(f.renderText(texto_imprimir))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    imprimir_con_fuente()