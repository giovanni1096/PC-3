import requests

def obtener_precio_bitcoin():
    try:
       
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        response = requests.get(url)
        data = response.json()
        precio_bitcoin_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        datos_formateados = f"Fecha: {data['time']['updated']}\nPrecio de 1 Bitcoin en USD: {precio_bitcoin_usd:,.4f}"

        with open("precio_bitcoin.txt", "w") as archivo:
            archivo.write(datos_formateados)

        print(f'Datos del precio de Bitcoin almacenados en "precio_bitcoin.txt"')

    except requests.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    obtener_precio_bitcoin()