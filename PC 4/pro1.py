import requests

def obtener_precio_bitcoin():
    try:
    
        n_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))

        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    
        response = requests.get(url)
        data = response.json()
        precio_bitcoin_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))

       
        costo_total_usd = n_bitcoins * precio_bitcoin_usd

        print(f"El costo actual de {n_bitcoins} Bitcoins en USD es: ${costo_total_usd:,.4f}")

    except ValueError:
        print("Error: Ingrese un valor numérico válido para la cantidad de bitcoins.")
    except requests.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    obtener_precio_bitcoin()