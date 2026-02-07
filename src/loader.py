import pandas as pd
from sqlalchemy import create_engine, text
import logging
import os

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(df, db_path='data/auroria_noticias.db', table_name='news_feed'):
    """
    Función encargada de persistir los datos limpios en una base de datos SQL.
    Recibe el DataFrame y la ruta donde se guardará el archivo .db.
    """
    if df.empty:
        logging.warning("Yo recibí datos vacíos. No haré ninguna carga a la base de datos.")
        return False

    try:
        # 1. Yo construyo la cadena de conexión (Connection String) para SQLite
        # SQLite necesita 3 barras /// para rutas relativas
        engine = create_engine(f'sqlite:///{db_path}')
        
        logging.info(f"Yo estoy conectando a la base de datos en: {db_path}")

        # 2. Yo cargo los datos
        # if_exists='append': Si la tabla ya existe, agrego los datos abajo (no borro lo anterior).
        # index=False: No guardo el índice numérico de Pandas (0, 1, 2...) porque no sirve en SQL.
        with engine.connect() as conn:
            df.to_sql(table_name, con=conn, if_exists='append', index=False)
            
            logging.info(f"Yo inserté exitosamente {len(df)} registros en la tabla '{table_name}'.")
            return True

    except Exception as e:
        logging.error(f"Yo fallé al intentar escribir en la base de datos: {e}")
        return False

if __name__ == "__main__":
    # --- PRUEBA UNITARIA ---
    # Yo me aseguro de que la carpeta 'data' exista, si no, la creo
    if not os.path.exists('data'):
        os.makedirs('data')

    # Creo un DataFrame pequeñito para probar la inserción
    df_prueba = pd.DataFrame({
        'title': ['Noticia de Prueba DB'],
        'content': ['Este contenido debe aparecer en SQLite'],
        'processed_at': ['2026-02-07 10:00:00']
    })
    
    print("--- Intentando Cargar ---")
    load_data(df_prueba)