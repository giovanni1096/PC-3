import requests
import sqlite3

def obtener_tipo_cambio_anual():
   
    usuario = "l giovanni"
    clave = "Giovanni67"

    url = f"https://api.sunat.cloud/valor-dolar?fecha=2023-01-01&usuario={usuario}&clave={clave}"

    try:
        
        response = requests.get(url)
        data = response.json()
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sunat_info (
                fecha TEXT PRIMARY KEY,
                precio_compra REAL,
                precio_venta REAL
            )
        ''')


        for registro in data:
            cursor.execute('''
                INSERT OR IGNORE INTO sunat_info (fecha, precio_compra, precio_venta)
                VALUES (?, ?, ?)
            ''', (registro['fecha'], registro['precio_compra'], registro['precio_venta']))

       
        conn.commit()
        print("Información almacenada en la base de datos.")

    except requests.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        conn.close()

def mostrar_contenido_tabla():
    try:
       
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM sunat_info")
        filas = cursor.fetchall()

        print("\nContenido de la tabla 'sunat_info':")
        for fila in filas:
            print(f"Fecha: {fila[0]}, Precio Compra: {fila[1]}, Precio Venta: {fila[2]}")

    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    obtener_tipo_cambio_anual()
    mostrar_contenido_tabla()