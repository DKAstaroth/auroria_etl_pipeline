import requests
import pandas as pd
import logging
from .interfaces import DataSource # Importamos el contrato

class APIExtractor(DataSource):
    """
    Implementación concreta: Extrae datos desde una API REST JSON.
    """
    def __init__(self, url: str):
        # Yo recibo la URL en el constructor, haciéndola configurable
        self.url = url
        self.logger = logging.getLogger(__name__)

    def extract(self) -> pd.DataFrame:
        try:
            self.logger.info(f"Yo (APIExtractor) estoy consultando: {self.url}")
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            df = pd.DataFrame(data)
            
            self.logger.info(f"Yo obtuve {len(df)} registros.")
            return df
            
        except requests.RequestException as e:
            self.logger.error(f"Yo fallé en la conexión: {e}")
            return pd.DataFrame()