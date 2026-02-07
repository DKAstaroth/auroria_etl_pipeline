import requests
import pandas as pd
import logging

# Configuro el logging para saber qué pasa dentro de este módulo
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data(url):
    """
    Función encargada de conectar con la fuente de datos externa (API)
    y traer la información cruda para su posterior procesamiento.
    """
    try:
        logging.info(f"Yo estoy iniciando la petición a la URL: {url}")
        
        # Yo realizo la petición GET con un timeout de 10 segundos para no bloquear el programa si la red falla
        response = requests.get(url, timeout=10)
        
        # Yo verifico si el estatus es 200 (OK). Si es 404 o 500, esto lanzará una excepción.
        response.raise_for_status()
        
        # Yo convierto la respuesta JSON en una estructura de datos de Python
        data = response.json()
        
        # Yo transformo esa lista de diccionarios en un DataFrame de Pandas
        df = pd.DataFrame(data)
        
        logging.info(f"Yo logré extraer {len(df)} registros exitosamente.")
        return df

    except requests.exceptions.RequestException as e:
        # Si algo falla en la conexión (DNS, internet caído, API caída), yo lo capturo aquí
        logging.error(f"Yo fallé al intentar conectar con la API: {e}")
        return pd.DataFrame() # Retorno un DataFrame vacío para que el pipeline no explote

    except Exception as e:
        # Cualquier otro error no previsto (ej. formato JSON inválido), yo lo atrapo aquí
        logging.error(f"Yo encontré un error inesperado procesando los datos: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Esta sección solo se ejecuta si yo corro este archivo directamente (para pruebas)
    test_url = "https://jsonplaceholder.typicode.com/posts"
    df_resultado = extract_data(test_url)
    print(df_resultado.head())