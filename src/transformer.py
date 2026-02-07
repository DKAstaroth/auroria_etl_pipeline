import pandas as pd
import logging
from datetime import datetime
from .interfaces import DataTransformer # Importamos el nuevo contrato

class NewsCleaner(DataTransformer):
    """
    Implementación concreta: Limpieza específica para NOTICIAS.
    Si mañana limpiamos Cripto, creamos otra clase 'CryptoCleaner'.
    """
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        logger = logging.getLogger(__name__)
        
        if df.empty:
            logger.warning("Yo recibí un DataFrame vacío. No hay nada que transformar.")
            return df

        try:
            logger.info("Yo (NewsCleaner) iniciando limpieza de noticias...")
            
            # Lógica de limpieza encapsulada
            df_clean = df.copy()
            
            # Renombrar columnas
            df_clean = df_clean.rename(columns={
                'userId': 'user_id',
                'id': 'external_id',
                'title': 'title',
                'body': 'content'
            })

            # Eliminar nulos
            initial_count = len(df_clean)
            df_clean = df_clean.dropna(subset=['title', 'content'])
            
            # Limpiar texto
            df_clean['content'] = df_clean['content'].str.replace('\n', ' ', regex=False)
            
            # Metadata
            df_clean['processed_at'] = datetime.now().isoformat()

            logger.info(f"Limpieza completada. {len(df_clean)} registros listos.")
            return df_clean

        except Exception as e:
            logger.error(f"Error en la transformación: {e}")
            return pd.DataFrame()