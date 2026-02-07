import pandas as pd
import logging
from datetime import datetime

# Configuro el logging para rastrear la limpieza
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transform_data(df):
    """
    Función encargada de limpiar, normalizar y enriquecer los datos.
    Recibe un DataFrame crudo y devuelve uno listo para la base de datos.
    """
    if df.empty:
        logging.warning("Yo recibí un DataFrame vacío. No hay nada que transformar.")
        return df

    try:
        logging.info("Yo estoy iniciando el proceso de transformación de datos...")
        
        # 1. Yo creo una copia para no afectar el objeto original en memoria
        df_clean = df.copy()

        # 2. Yo renombro las columnas para seguir el estándar de bases de datos (snake_case)
        # De 'userId' a 'user_id', etc.
        df_clean = df_clean.rename(columns={
            'userId': 'user_id',
            'id': 'external_id',
            'title': 'title',
            'body': 'content'
        })

        # 3. Yo elimino filas que no tengan título o contenido (datos basura)
        # En el mundo real, a veces llegan noticias vacías que rompen el análisis
        initial_count = len(df_clean)
        df_clean = df_clean.dropna(subset=['title', 'content'])
        
        if len(df_clean) < initial_count:
            logging.info(f"Yo eliminé {initial_count - len(df_clean)} filas con datos faltantes.")

        # 4. Yo limpio el texto: elimino saltos de línea (\n) excesivos en el contenido
        # Esto facilita el procesamiento de lenguaje natural (NLP) posterior
        df_clean['content'] = df_clean['content'].str.replace('\n', ' ', regex=False)

        # 5. Yo añado una columna de metadatos: ¿Cuándo procesé esto?
        # Fundamental para auditoría
        df_clean['processed_at'] = datetime.now().isoformat()

        logging.info(f"Yo terminé la transformación. Datos listos: {len(df_clean)} filas.")
        return df_clean

    except Exception as e:
        logging.error(f"Yo fallé durante la transformación de datos: {e}")
        return pd.DataFrame() # Retorno vacío en caso de error crítico

if __name__ == "__main__":
    # --- PRUEBA UNITARIA ---
    # Yo simulo datos sucios para probar mi lógica
    data_prueba = {
        'userId': [1, 2, 3],
        'id': [101, 102, 103],
        'title': ['Noticia 1', None, 'Noticia 3'], # El segundo tiene None (debe borrarse)
        'body': ['Texto\ncon\nenters', 'Texto normal', 'Texto final']
    }
    df_raw = pd.DataFrame(data_prueba)
    
    print("--- ANTES ---")
    print(df_raw)
    
    df_result = transform_data(df_raw)
    
    print("\n--- DESPUÉS ---")
    print(df_result)