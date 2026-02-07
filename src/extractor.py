import aiohttp
import asyncio
import pandas as pd
import logging
from .interfaces import DataSource

class AsyncAPIExtractor(DataSource):
    """
    Extractor de Alto Rendimiento (AsyncIO).
    """
    def __init__(self, url: str, limit: int = 100):
        self.base_url = url
        self.limit = limit
        self.logger = logging.getLogger(__name__)

    async def fetch_one(self, session, id_noticia):
        """
        Baja UNA noticia de forma asíncrona.
        """
        url = f"{self.base_url}/{id_noticia}"
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                # A veces la API devuelve {} para IDs que no existen, lo manejamos
                if not data: 
                    return None
                return data
        except Exception as e:
            self.logger.error(f"Error bajando noticia {id_noticia}: {e}")
            return None

    async def extract(self) -> pd.DataFrame:
        self.logger.info(f"Iniciando descarga ASÍNCRONA de {self.limit} noticias...")
        
        async with aiohttp.ClientSession() as session:
            # Creamos la lista de tareas (peticiones en paralelo)
            tasks = [self.fetch_one(session, i) for i in range(1, self.limit + 1)]
            
            # Disparamos todas a la vez
            results = await asyncio.gather(*tasks)
            
        # Filtramos los None (errores o vacíos)
        clean_results = [r for r in results if r is not None]
        
        df = pd.DataFrame(clean_results)
        self.logger.info(f"Descarga finalizada. {len(df)} registros obtenidos.")
        return df