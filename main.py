import logging
from src.extractor import extract_data
from src.transformer import transform_data
from src.loader import load_data

# Configuración global del log para que se guarde en un archivo y también salga por pantalla
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/pipeline.log"), # Yo guardo el historial aquí
        logging.StreamHandler() # Yo también muestro el log en la terminal
    ]
)

def run_pipeline():
    """
    Función principal que orquesta todo el flujo ETL.
    """
    logging.info("--- INICIANDO PROCESO AUROR-IA ETL ---")
    
    # 1. Definir la Fuente (En el futuro será una API de noticias real)
    URL_FUENTE = "https://jsonplaceholder.typicode.com/posts"
    
    # 2. Paso de Extracción
    logging.info("Paso 1: Iniciando Extracción...")
    df_raw = extract_data(URL_FUENTE)
    
    if df_raw.empty:
        logging.error("El proceso se detuvo porque la extracción falló.")
        return

    # 3. Paso de Transformación
    logging.info("Paso 2: Iniciando Transformación...")
    df_clean = transform_data(df_raw)
    
    if df_clean.empty:
        logging.error("El proceso se detuvo porque la transformación dejó los datos vacíos.")
        return

    # 4. Paso de Carga
    logging.info("Paso 3: Iniciando Carga a Base de Datos...")
    # Guardamos en la carpeta data/
    exito = load_data(df_clean, db_path='data/auroria_noticias.db')
    
    if exito:
        logging.info("--- PROCESO COMPLETADO CON ÉXITO ---")
    else:
        logging.error("--- EL PROCESO FALLÓ EN LA ETAPA DE CARGA ---")

if __name__ == "__main__":
    run_pipeline()