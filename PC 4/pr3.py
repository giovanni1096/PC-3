import requests
import os
import zipfile

def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    with open(nombre_archivo, 'wb') as f:
        f.write(response.content)

def comprimir_imagen(nombre_imagen, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as zip_file:
        zip_file.write(nombre_imagen)

def descomprimir_zip(nombre_zip, directorio_destino):
    with zipfile.ZipFile(nombre_zip, 'r') as zip_file:
        zip_file.extractall(directorio_destino)

if __name__ == "__main__":
   
    url_imagen = "C:\Users\luisg\OneDrive\Escritorio\pro3.jpeg"

   
    nombre_imagen = "imagen_descargada.jpeg"
    descargar_imagen(url_imagen, nombre_imagen)
    print(f'Imagen descargada desde "{url_imagen}" y almacenada como"{nombre_imagen}"')

    nombre_zip = "C:\Users\luisg\OneDrive\Escritorio\pro3.zip"
    comprimir_imagen(nombre_imagen, nombre_zip)
    print(f'Imagen "{nombre_imagen}" comprimida en "{nombre_zip}"')
  
    directorio_destino = "directorio_descomprimido"
    os.makedirs(directorio_destino, exist_ok=True)
    descomprimir_zip(nombre_zip, directorio_destino)
    print(f'Archivo zip "{nombre_zip}" descomprimido en "{directorio_destino}"')