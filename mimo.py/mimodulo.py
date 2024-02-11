import random

def generar_numeros_aleatorios(cantidad):
    
    return [random.randint(0, 100) for _ in range(cantidad)]

def mostrar_lista(lista):

    print("Lista generada:", lista)

def ordenar_y_mostrar(lista):
 
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)