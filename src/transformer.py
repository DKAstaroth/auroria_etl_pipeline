import pandas as pd
import logging
from datetime import datetime
from textblob import TextBlob # Importamos el cerebro
from .interfaces import DataTransformer

class NewsCleaner(DataTransformer):
    """
    Componente encargado de limpiar, normalizar y ENRIQUECER los datos.
    """
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        logger = logging.getLogger(__name__)
        
        if df.empty:
            logger.warning("DataFrame vacío. Nada que transformar.")
            return df

        try:
            logger.info("Iniciando transformación y enriquecimiento con NLP...")
            
            df_clean = df.copy()
            
            # 1. Normalización (Igual que antes)
            df_clean = df_clean.rename(columns={
                'userId': 'user_id',
                'id': 'external_id',
                'title': 'title',
                'body': 'content'
            })

            # 2. Limpieza básica
            df_clean = df_clean.dropna(subset=['title', 'content'])
            df_clean['content'] = df_clean['content'].astype(str).str.replace('\n', ' ', regex=False)
            
            # --- 3. LA INTELIGENCIA ARTIFICIAL (NLP) ---
            # Aplicamos análisis de sentimiento a cada fila
            # TextBlob devuelve una polaridad de -1 a 1
            logger.info("Calculando sentimiento de las noticias...")
            
            df_clean['sentiment_score'] = df_clean['content'].apply(
                lambda text: TextBlob(text).sentiment.polarity
            )

            # Clasificación humana para facilitar lectura en DB
            def classify_sentiment(score):
                if score > 0.1: return 'POSITIVE'
                if score < -0.1: return 'NEGATIVE'
                return 'NEUTRAL'

            df_clean['sentiment_label'] = df_clean['sentiment_score'].apply(classify_sentiment)
            
            # 4. Metadata
            df_clean['processed_at'] = datetime.now().isoformat()

            logger.info(f"Transformación completada. {len(df_clean)} registros enriquecidos.")
            return df_clean

        except Exception as e:
            logger.error(f"Error crítico en la transformación: {e}")
            return pd.DataFrame()