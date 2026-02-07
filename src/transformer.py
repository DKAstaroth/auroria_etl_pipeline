import pandas as pd
import logging
from datetime import datetime
from .interfaces import DataTransformer

class NewsCleaner(DataTransformer):
    """
    Componente encargado de limpiar y normalizar los datos.
    Implementa la interfaz DataTransformer.
    """
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        logger = logging.getLogger(__name__)
        
        if df.empty:
            logger.warning("Recibí un DataFrame vacío. Nada que transformar.")
            return df

        try:
            logger.info("Iniciando limpieza de datos...")
            
            # 1. Crear copia para no afectar memoria original
            df_clean = df.copy()
            
            # 2. Renombrar columnas (Normalización)
            # Nota: Al usar la API asíncrona, a veces los campos pueden variar ligeramente
            # pero asumimos la estructura estándar de JSONPlaceholder
            df_clean = df_clean.rename(columns={
                'userId': 'user_id',
                'id': 'external_id',
                'title': 'title',
                'body': 'content'
            })

            # 3. Eliminar filas vacías
            df_clean = df_clean.dropna(subset=['title', 'content'])
            
            # 4. Limpieza de texto (Quitar saltos de línea molestos)
            if 'content' in df_clean.columns:
                df_clean['content'] = df_clean['content'].astype(str).str.replace('\n', ' ', regex=False)
            
            # 5. Agregar Metadata (Timestamp)
            df_clean['processed_at'] = datetime.now().isoformat()

            logger.info(f"Limpieza completada. {len(df_clean)} registros listos.")
            return df_clean

        except Exception as e:
            logger.error(f"Error en la transformación: {e}")
            return pd.DataFrame()